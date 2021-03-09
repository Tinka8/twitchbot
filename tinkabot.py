import os
import random
import time
from twitchio.ext import commands
from resources.heroes import heroes
from resources.heroes import structuredHeroes
from resources.winsloses import getWinsAndLoses
from resources.commands import fullList
from resources.commands import supported
from resources.winsloses import getRecentMatches 

bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)



# wrapper for await and append 
async def replaceSelected(ctx, selected):
    await ctx.send(selected)
    picked.append(selected)                                                        

# wrapper for getRecentMatches with cast to json 
def getRecentMatchesJson(playerId): 
    results = getRecentMatches(playerId)
    return results.json()  



# list of already picked heroes
picked = []

# pick hero from arrays of heroes
def selectHero(message = '!pick'):
    if message in ('!carry', '!pick 1'):
        return random.choice(structuredHeroes['pos1'])
    elif message in ('!mid', '!pick 2'):
        return random.choice(structuredHeroes['pos2'])
    elif message in ('!off', '!offlane', '!offka', '!pick 3'):
        return random.choice(structuredHeroes['pos3'])
    elif message in ('!jungle', '!pick 4'):
        return random.choice(structuredHeroes['pos4'])
    elif message == ('!support'):
        return random.choice(structuredHeroes['pos4'] + structuredHeroes['pos5'])
    elif message in ('!suck', '!pick 5'):
        return random.choice(structuredHeroes['pos5'])
    else:
        return random.choice(heroes)



# ! pick command
@bot.command(name='pick', aliases = ['carry', 'support', 'jungle','off', 'offlane','offka','mid','suck','jungle'])                                          
async def pick(ctx):
    selected = selectHero(ctx.content)    
    
    await replaceSelected(ctx, selected)

# ! repick command
@bot.command(name='repick')
async def repick(ctx):
    if (len(picked) >= len(heroes)):
        await ctx.send('Všetci hrdinovia už boli picknutí')
        
        return False

    selected = selectHero()
    if selected in picked:
        await repick(ctx)
        
        return False 

    await replaceSelected(ctx, selected)
    
# ! wl command
@bot.command(name='wl')
async def wl(ctx):
    hours = time.time() - (5 * 3600)
    results = getWinsAndLoses(os.environ['PLAYER_ID'], hours)
    
    await ctx.send(str(results['wins']) + 'W - ' + str(results['loses']) + 'L')

# ! commands command
@bot.command(name='commands')
async def commands(ctx):
    line = ''
    
    for item in supported:
        line = line + item + ', '
    
    await ctx.send('List of commands: ' + line.rstrip(', '))

# ! help command
@bot.command(name='help')
async def help(ctx):
    message = ''
    
    for command in fullList:
        description = fullList[command]
        message = message + command + ' - ' + description + ', '
    
    await ctx.send(message.rstrip(', '))

# ! kda command
@bot.command(name='kda')
async def kda(ctx):
    kills = 0
    assists = 0
    deaths = 0
    result = 0

    json = getRecentMatchesJson(42943450)
    hours = time.time() - (5 * 3600)

    for match in json:
        
        if (match['start_time'] > hours):

            kills = kills + match['kills']
            assists = assists + match['assists']
            deaths = deaths + match['deaths']
            
    if deaths == 0:
        result = (kills + assists)
    else:
        result = (kills + assists) / deaths 

    await ctx.send(round(result,2))

# ! topkda commmand
@bot.command(name='topkda')
async def topkda(ctx):
    kills = 0
    assists = 0
    deaths = 0
    result = 0
    top = 0

    json = getRecentMatchesJson(42943450)
    hours = time.time() - (5 * 3600)

    for match in json:
        
        if (match['start_time'] > hours):

            kills = kills + match['kills']
            assists = assists + match['assists']
            deaths = deaths + match['deaths']
    
    if deaths == 0:
        result = (kills + assists)
    else:
        result = (kills + assists) / deaths
    
    if result > top:
        top = result 

    await ctx.send(str(match['kills']) + '/' + str(match['deaths']) + '/' + str(match['assists']) + ' - ' + str(round(top,2)))

# ! wr command
@bot.command(name='wr')
async def wr(ctx):
    winrate = 0
    output = {
        'wins': 0,
        'loses': 0
    }
    
    json = getRecentMatchesJson(42943450)

    for match in json:
        # fatallik was radiant and won 
        if match['radiant_win'] == True and match['player_slot'] <= 127:          
            output['wins'] += 1

         # fatallik was radiant and lost
        elif match['radiant_win'] == True and match['player_slot'] >= 127:        
            output['loses'] += 1

        # fatallik was dire and won
        elif match['radiant_win'] == False and match['player_slot'] >= 128:      
            output['wins'] += 1

        # fatallik was dire and lost
        elif match['radiant_win'] == False and match['player_slot'] <= 128:       
            output['loses'] += 1

    winrate = (output['wins'] / len(json)) * 100

    await ctx.send(str(round(winrate,2)) + '% ' + '(za posledných 20 zápasov)')

# ! versatility command
@bot.command(name='versatility')
async def versatility(ctx):
    # list of heroes id played in last 20 matches
    versatility = []

    json = getRecentMatchesJson(42943450)

    for match in json:
        hero = versatility.append(match['hero_id'])

    count = set(versatility)

    await ctx.send(str(len(count)) + ' ' + '(za posledných 20 zápasov)')

# ! top10 command
@bot.command(name='top10')
async def top10(ctx):
    
    response = requests.get('https://api.opendota.com/api/players/' + str(os.environ['PLAYER_ID']) + '/heroes')
    heroes = response.json()
   
    response = requests.get('https://api.opendota.com/api/heroes')
    names = response.json()
    
    unsorted = {}

    for hero in heroes:
        
        if hero['games'] > 5:
            
            unsorted[hero['hero_id']] = round((hero['win'] / hero['games']) * 100, 2)
    
    resorted = dict(sorted(unsorted.items(), key=lambda item: item[1], reverse=True))

    resorted = list(resorted.items())[:10]

    human = []

    for hero in resorted:

        rate = hero[1]

        hero_name = ''

        for name in names:
            
            if int(name['id']) == int(hero[0]):
                hero_name = name['localized_name']

        human.append({
            'hero_name': hero_name,
            'rate': rate
        })

    message = ''
        
    for item in human:
        message = message + ' ' + item['hero_name'] + ' - ' + str(item['rate']) + '% '
    
    await ctx.send(message)



if __name__ == '__main__':
    bot.run()


