# bot.py
import os

import discord

# set DISCORD_TOKEN=yourtoken
# or with bash: 
# export DISCORD_TOKEN=yourtoken

TOKEN = os.environ['DISCORD_TOKEN']
GUILD = os.environ['DISCORD_GUILD']

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

#@client.event
#async def on_ready():
#    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
