import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Bot Activated')

authorized_users = [your user id]
role_ids = [your admin role id]

@client.event
async def on_message(message):
    if message.content.startswith('!admin') or message.content.startswith('!de-admin'):
        if message.author.id in authorized_users:
            if message.content.startswith('!admin'):
                member = message.mentions[0] if len(message.mentions) > 0 else None
                if member is not None:
                    for role_id in role_ids:
                        role = discord.utils.get(message.guild.roles, id=role_id)
                        if role:
                            await member.add_roles(role)
                            await message.channel.send(f'{member.mention} has been given the role.')
                            break
                    else:
                        await message.channel.send('Sorry, I could not find a valid role.')
                else:
                    await message.channel.send('Sorry, I could not find that member.')
            elif message.content.startswith('!de-admin'):
                member = message.mentions[0] if len(message.mentions) > 0 else None
                if member is not None:
                    for role_id in role_ids:
                        role = discord.utils.get(message.guild.roles, id=role_id)
                        if role:
                            await member.remove_roles(role)
                            await message.channel.send(f'{member.mention} no longer has the role.')
                            break
                    else:
                        await message.channel.send('Sorry, I could not find a valid role.')
                else:
                    await message.channel.send('Sorry, I could not find that member.')
        else:
            await message.channel.send(f'Hey, <@{authorized_users[0]}>, this idiot {message.author.mention} tried to use the admin command. what a loser lol')

client.run('YOUR BOT TOKEN')
