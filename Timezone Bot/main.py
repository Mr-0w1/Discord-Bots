import discord
from discord import app_commands
from discord.ext import commands
import time

client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

gmt = time.gmtime()
bst = time.localtime()
cet = time.gmtime(time.mktime(time.gmtime()) + 3600)
est = time.gmtime(time.mktime(gmt) - 5 * 3600)
cst = time.gmtime(time.mktime(gmt) - 6 * 3600)
mst = time.gmtime(time.mktime(gmt) - 7 * 3600)
pst = time.gmtime(time.mktime(gmt) - 8 * 3600)
akst = time.gmtime(time.mktime(gmt) - 9 * 3600)
hst = time.gmtime(time.mktime(gmt) - 10 * 3600)
cest = time.gmtime(time.mktime(time.gmtime()) + 7200)

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

@client.tree.command(name='help', description='gives help')
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hello {interaction.user.mention}, I am a bot that tells people what time it is in any timezone. Do /timezone then the timezone you want. e.g /timezone gmt. and do .sync to sync all of the commands.')
 
@client.tree.command(name='timezone', description='tells you what time it is in different timezone')
@app_commands.describe(timezone='What Timezone do you want?')
@app_commands.choices(timezone=[
    discord.app_commands.Choice(name='gmt', value=1),
    discord.app_commands.Choice(name='est', value=2),
    discord.app_commands.Choice(name='cst', value=3),
    discord.app_commands.Choice(name='mst', value=4),
    discord.app_commands.Choice(name='pst', value=5),
    discord.app_commands.Choice(name='akst', value=6),
    discord.app_commands.Choice(name='hst', value=7),
    discord.app_commands.Choice(name='bst', value=8),
    discord.app_commands.Choice(name='cet', value=9),
    discord.app_commands.Choice(name='cest', value=10),
])
async def timezone(interaction: discord.Interaction, timezone: discord.app_commands.Choice[int]):
    if timezone.name == 'gmt':
        time_str = time.strftime('%H:%M', gmt)
    elif timezone.name == 'est':
        time_str = time.strftime('%H:%M', est)
    elif timezone.name == 'cst':
        time_str = time.strftime('%H:%M', cst)
    elif timezone.name == 'mst':
        time_str = time.strftime('%H:%M', mst)
    elif timezone.name == 'pst':
        time_str = time.strftime('%H:%M', pst)
    elif timezone.name == 'akst':
        time_str = time.strftime('%H:%M', akst)
    elif timezone.name == 'hst':
        time_str = time.strftime('%H:%M', hst)
    elif timezone.name == 'bst':
        time_str = time.strftime('%H:%M', bst)
    elif timezone.name == 'cet':
        time_str = time.strftime('%H:%M', cet)
    elif timezone.name == 'cest':
        time_str = time.strftime('%H:%M', cest)
    await interaction.response.send_message(f'{interaction.user.mention}, The time in {timezone.name} is: {time_str}')


client.run('Token')