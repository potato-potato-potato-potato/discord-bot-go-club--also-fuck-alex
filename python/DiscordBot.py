import os
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv

from discordBotCommands import _StoreDiscordChannelInvite
from discordBotCommands import _banFlip
from discordBotCommands import _frame

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Setting up bot
intents = discord.Intents.default()
intents.members = True
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix=';', intents=intents)

# display a message in console to tell admins that the bot is online

"""
Bot Events

"""
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
  await _StoreDiscordChannelInvite(guild)


"""
Bot Admin Commands
"""

@bot.command(name="banFlip", help="||50% chance for you to get banned, 50% chance for your opponent to get banned")
async def ban_flip(ctx, *, arg):
  await _banFlip(ctx, arg)

@bot.command(name="frame", help="|| The butler was killed")
async def frame(ctx, *, args):
  await _frame(bot, ctx, args)

bot.run(TOKEN)
