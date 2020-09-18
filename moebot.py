import discord
from discord.ext import commands
import random
import glob
import os

# setup your bot first in discord web interface
# https://realpython.com/how-to-make-a-discord-bot-python/

# You can use anaconda on a windows or linux box
# or python on your raspberry pi

# python3 moebot.py

# command are started with ?
# ?help
# ?roll 4d6
# ?moe

TOKEN = 'YOURTOKEN'
GUILD = 'YOURSERVERNAME'

description = '''moeBot in Python'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@bot.command()
async def hello(ctx):
    """Says world"""
    await ctx.send("world")


@bot.command()
async def add(ctx, left : int, right : int):
    """Adds two numbers together."""
    await ctx.send(left + right)
    
@bot.command()
async def sayuser(ctx):
    """get user name"""
    user = ctx.message.author
    await ctx.send("mention: " + user.mention + " name: " + user.name)
    
@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    total = 0
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))

    for r in result.split(','):
        total += int(r.strip())

    await ctx.send("__Your results for **" + str(rolls) + "** D**" + str(limit) + "**__\n" + ":game_die: " +  result + "\nTotal [**" + str(total) +  "**]")

@bot.command()
async def moe(ctx):
    """Random monster girl from Moero Chroncile."""
    mgirls = sorted(glob.glob("C:\\Users\\moe\\discordpycode\\moecron\\*.jpg"))
    value = random.randint(1, len(mgirls))
    thegirl = os.path.basename(mgirls[value-1])
    channel = ctx.message.channel
    await channel.send(file=discord.File(mgirls[value-1]))
