import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Bot activated')
    while True:
        thing = input("Enter something: ")
        channel = client.get_channel(channel-to-send-to) 
        await channel.send(thing)

client.run('Token')
