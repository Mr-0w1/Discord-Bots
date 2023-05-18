import discord
from discord import app_commands
from discord.ext import commands

client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Bot Activated')

authorized_users = [user 1 id, user 2 id]
roles = ['admin', 'Admin']

@client.event
async def on_message(message):
    if message.content.startswith('!admin') or message.content.startswith('!de-admin'):
        if message.author.id in authorized_users:
            if message.content.startswith('!admin'):
                member = message.mentions[0] if len(message.mentions) > 0 else None
                if member is not None:
                    role_name = 'admin'
                    if role_name in roles:
                        role = discord.utils.get(message.guild.roles, name=role_name)
                        await member.add_roles(role)
                        await message.channel.send(f'{member.mention} has been given the {role_name} role.')
                    else:
                        await message.channel.send(f'Sorry, {role_name} is not a valid role.')
                else:
                    await message.channel.send('Sorry, I could not find that member.')
            elif message.content.startswith('!de-admin'):
                member = message.mentions[0] if len(message.mentions) > 0 else None
                if member is not None:
                    role_name = 'admin'
                    if role_name in roles:
                        role = discord.utils.get(message.guild.roles, name=role_name)
                        await member.remove_roles(role)
                        await message.channel.send(f'{member.mention} no longer has the {role_name} role.')
                    else:
                        await message.channel.send(f'Sorry, {role_name} is not a valid role.')
                else:
                    await message.channel.send('Sorry, I could not find that member.')
        else:
            await message.channel.send(f'Hey, <@{authorized_users[0]}> and <@{authorized_users[1]}>, this idiot {message.author.mention} tried to use the admin command. what a loser lol')


client.run('Token')
