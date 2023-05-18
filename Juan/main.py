import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@client.event
async def on_connect():
    print("I am connected!")

@client.event
async def on_disconnect():
    print("I have been disconnected!")

async def ping(message):
    with open('JUAN.jpg', 'rb') as f:
        image = discord.File(f)
        await message.channel.send('<@person to annoy id>', file=image)

@client.event
async def on_message(message):
    if message.content.startswith("!juan"):
        print('juan')
        await ping(message)

client.run('Token')
