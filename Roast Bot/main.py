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

@client.tree.command(name='roast', description='roasts you')
async def roast(interaction: discord.Interaction):
        roasts = [    
    "yo mama so fat when she walked in front of the TV, I missed 23 seasons of The Simpsons.",
    "you're so short, I almost mistook you for a traffic cone.",
    "yo mama is so old, when she was in school, history was called current events.",
    "you're so lazy, you need an appointment just to wake up in the morning.",
    "yo mama is so slow, she has to chase the ice cream truck.",
    "you're so cheap, you bring a shopping cart to the dollar store.",
    "yo mama is so clumsy, she can trip over a cordless phone.",
    "you're so boring, your pet rock died of boredom.",
    "yo mama is so short, she pole-dances on a candy cane.",
    "you're so forgetful, you forgot your own birthday.",
    "yo mama is so fat, she doesn't need the internet; she's already worldwide.",
    "you're so indecisive, you couldn't choose a side of the bed to wake up on."
    ]
        
        chosen_string = random.choice(roasts)
        await interaction.response.send_message(f'{interaction.user.mention}, {chosen_string}')

client.run('Token')
