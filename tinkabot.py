import os
import random
from twitchio.ext import commands

bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)


@bot.command(name='test')
async def test(ctx):
    await ctx.send('Funguje to')

@bot.command(name='tina')
async def tina(ctx):
    await ctx.send('jsem tina, je mi 17 a uz 4 roky piju kavu')

@bot.command(name='pick')
async def pick(ctx):
    heroes = [
        "Slark",
        "Oracle",
        "Bane",
        "Axe"
    ]
    await ctx.send(random.choice(heroes))


if __name__ == "__main__":
    bot.run()

