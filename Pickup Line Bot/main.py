import discord
from discord import app_commands
from discord.ext import commands
import random

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

@client.tree.command(name='pickupline', description='sends a random pickupline')
async def pickupline(interaction: discord.Interaction):
        line = [
    "Are you a parking ticket? 'Cause you've got 'fine' written all over you.",
    "Are you a magician? Every time I look at you, everyone else disappears.",
    "Do you have a map? I keep getting lost in your eyes.",
    "You must be a broom, 'cause you swept me off my feet.",
    "Are you an alien? Because you just abducted my heart.",
    "You're so hot, you're making my allergies act up.",
    "Are you a camera? Because every time I look at you, I smile.",
    "Do you have a Band-Aid? I just scraped my knee falling for you.",
    "Do you have a sunburn or are you always this hot?",
    "Are you a thief? 'Cause you just stole my heart.",
    ]

        chosen_string = random.choice(line)
        await interaction.response.send_message(f'{interaction.user.mention}, {chosen_string}')

client.run('Token')