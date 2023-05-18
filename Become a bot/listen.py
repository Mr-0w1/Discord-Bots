import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Bot activated')

@client.event
async def on_message(message):
    print(f"{message.author}: {message.content}")

client.run('Token')
