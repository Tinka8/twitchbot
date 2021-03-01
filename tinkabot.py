import os
import random
import time
from twitchio.ext import commands
from resources.heroes import heroes
from resources.heroes import structuredHeroes
from resources.winsloses import getWinsAndLoses
from resources.commands import fullList

bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)



# replacing await and append 
async def replaceSelected(ctx, selected):
    await ctx.send(selected)
    picked.append(selected)                                                        

# ! test command
@bot.command(name='test')                                             
async def test(ctx):
    await ctx.send('Funguje to')

# ! tina command 
@bot.command(name='tina')                                              
async def tina(ctx):
    await ctx.send('jsem tina, je mi 17 a uz 4 roky piju kavu')       



# list of already picked heroes
picked = [

]



# pick hero from arrays of heroes
def selectHero(message = "!pick"):
    if message in ("!carry", "!pick 1"):
        return random.choice(structuredHeroes["pos1"])
    elif message in ("!mid", "!pick 2"):
        return random.choice(structuredHeroes["pos2"])
    elif message in ("!off", "!offlane", "!offka", "!pick 3"):
        return random.choice(structuredHeroes["pos3"])
    elif message in ("!jungle", "!pick 4"):
        return random.choice(structuredHeroes["pos4"])
    elif message == ("!support"):
        return random.choice(structuredHeroes["pos4"] + structuredHeroes["pos5"])
    elif message in ("!suck", "!pick 5"):
        return random.choice(structuredHeroes["pos5"])
    else:
        return random.choice(heroes)



# ! pick command
@bot.command(name='pick', aliases = ["carry", "support", "jungle","off", "offlane","offka","mid","suck","jungle"])                                          
async def pick(ctx):
    selected = selectHero(ctx.content)    
    
    await replaceSelected(ctx, selected)

# ! repick command
@bot.command(name='repick')
async def repick(ctx):
    if (len(picked) >= len(heroes)):
        await ctx.send("Všetci hrdinovia už boli picknutí")
        return False

    selected = selectHero()
    if selected in picked:
        await repick(ctx)
        return False 

    await replaceSelected(ctx, selected)

# ! chant command
@bot.command(name='chant')
async def chant(ctx):
    for i in range(0,6,+1):
        await ctx.send((i-1)*"* ")

    await ctx.send("* * * * * fatal")

    for j in reversed(range(0,6,+1)):
        await ctx.send((j-1)*"* ")
    
# ! wl command
@bot.command(name='wl')
async def wl(ctx):
    hours = time.time() - (5 * 3600)
    results = getWinsAndLoses(os.environ['PLAYER_ID'], hours)
    
    await ctx.send(str(results["wins"]) + "W - " + str(results["loses"]) + "L")

# ! commands command
@bot.command(name='commands')
async def commands(ctx):
    supported = ['!pick', '!repick', '!tina', '!test', '!wl', '!kda', '!chant']
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



if __name__ == "__main__":
    bot.run()


