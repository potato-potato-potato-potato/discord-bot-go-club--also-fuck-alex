import os
import random
import discord


from discord.ext import commands
from dotenv import load_dotenv
from datetime import timedelta, datetime


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
date = None

bot = commands.Bot(command_prefix='-')

# display a message in console to tell admins that the bot is online
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# @bot.event
# async def on_message(message):
#     bot.wait_until_ready()
#     x = random.randint(0, 100)
#     if x == 69:
#         await message.send("https://www.change.org/plzsign_1_")
#     await bot.process_commands(message)




# When ever a new member joins, the bot will send them a dm to welcome them
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the go server !'
    )



# give meeting time
@bot.command(name='settime', help="Sets the meeting time")
@commands.has_any_role('Officer','Teacher', 483412758621323264)
async def setMeetingTime(ctx, *, message):
    global date
    date = message


#next  
@bot.command(name='meeting', help="||Tell you next metting time or something")
async def nine_nine(ctx):
    if ctx.author == bot.user:
        return
    print(date)
    await ctx.reply(date)

#bans a user with a reason
# @bot.command(name='test', help="|| test command don't tuch")
# @commands.has_permissions(ban_members = True)
# async def ban(ctx, member : discord.Member, *, reason = None):
#     await member.ban(reason = reason)

# #give role to a member
@bot.command()
async def giverole(ctx, arg: discord.Member):
    await ctx.send(arg)
    knownrole = discord.utils.get(ctx.guild.roles, name="Mod")
    await arg.add_roles(knownrole)

# #spam
# @bot.command(name='spam')
# async def nine_nine(ctx):
#     for i in range (10):
#         await ctx.send("@everyone")
#         i=i+1




bot.run(TOKEN)
