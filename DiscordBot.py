import os
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv

from discordBotCommands import StoreDiscordChannelInvite


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix=';')

# display a message in console to tell admins that the bot is online
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# When ever a new member joins, the bot will send them a dm to welcome them
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the go server !'
    )

@bot.event
async def on_guild_join(guild):
  await StoreDiscordChannelInvite(guild)

@bot.command(name='test', help="Runs test commands")
async def test(ctx):
  guild = ctx.guild
  await StoreDiscordChannelInvite(guild)

# give next meeting time
@bot.command(name='meeting', help="||Tell you next metting time or something")
async def setMeeting(ctx):
    if ctx.author == bot.user:
        return
    await ctx.reply("Next meeting is 8/20 at lunch")

bot.run(TOKEN)
