import os
import random
from twitchio.ext import commands
from resources.heroes import heroes
from resources.heroes import pos1
from resources.heroes import pos2
from resources.heroes import pos3
from resources.heroes import pos4
from resources.heroes import pos5

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


picked = [

]


def selectHero(message = "!pick"):
    if (message in ["!carry", "!pick 1"]):
        return random.choice(pos1)
    elif (message in ["!mid", "!pick 2"]):
        return random.choice(pos2)
    elif (message in ["!off", "!offlane", "!offke", "!pick 3"]):
        return random.choice(pos3)
    elif (message in ["!jungle", "!pick 4"]):
        return random.choice(pos4)
    elif (message == "!support"):
        return random.choice(pos4 + pos5)
    elif (message in ["!suck", "!pick 5"]):
        return random.choice(pos5)
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




if __name__ == "__main__":
    bot.run()


