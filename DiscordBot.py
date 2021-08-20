import os
import random
import discord
import Client

from discord.ext import commands
from dotenv import load_dotenv
from datetime import timedelta, datetime


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
date = None

bot = commands.Bot(command_prefix='/')

# display a message in console to tell admins that the bot is online
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(ctx):
    bot.wait_until_ready()
    x = random.randint(0, 2)
    if x == 2:
        await ctx.send("https://www.change.org/plzsign_1_")
    await bot.process_commands(ctx)




# When ever a new member joins, the bot will send them a dm to welcome them
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the go server !'
    )



# give next meeting time
@bot.command(name='meeting', help="||Tell you next metting time or something")
async def nine_nine(ctx):
    if ctx.author == bot.user:
        return
    await ctx.reply("Next meeting is 8/20 at lunch")

#bans a user with a reason
@bot.command(name='test', help="|| test command don't tuch")
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

#give role to a member
@bot.command()
async def giverole(ctx, arg: discord.Member):
    await ctx.send(arg)
    knownrole = discord.utils.get(ctx.guild.roles, name="test")
    await arg.add_roles(knownrole)

#spam
@bot.command(name='spam')
async def nine_nine(ctx):
    for i in range (10):
        await ctx.send("@everyone")
        i=i+1




bot.run(TOKEN)
