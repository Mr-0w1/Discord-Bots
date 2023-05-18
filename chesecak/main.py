import discord
from discord import app_commands
from discord.ext import commands
import PIL
from PIL import Image

client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Bot Activated')
    try:
        synced = await client.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(e)
        await print('An error occurred while syncing commands')

@client.event
async def on_message(message):
    if message.content == '.sync':
        try:
            synced = await client.tree.sync()
            print(f'Synced {len(synced)} command(s)')
            await message.channel.send(f'Synced {len(synced)} command(s)')
        except Exception as e:
            print(e)
            await message.channel.send('An error occurred while syncing commands')

@client.tree.command(name='ping', description='pong')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'pong')

@client.tree.command(name='chesecak', description='chesecak')
async def ping(interaction: discord.Interaction):
    with open('chesecak.png', 'rb') as f:
        image = discord.File(f)
    await interaction.response.send_message(f'chesecak🤤', file=image)

client.run('Token')