import io

from discordSimplified import find_guild_member_from_mention
from discord import File

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

async def _frame(bot, ctx, args):
  
  user_mention = args.split(" | ")[0] 
  text_to_display = args.split(" | ")[1]
  
  userToFrame = await find_guild_member_from_mention(ctx.guild, user_mention)

  user_image = userToFrame.avatar_url_as(format="png")

  framedImage = createFramedImage(getDisplayName(userToFrame), await get_avatar_image_as_bytes(user_image), text_to_display)
  
  with io.BytesIO() as image_binary:
    framedImage.save(image_binary, "PNG")
    image_binary.seek(0)
    finalImageFile = File(fp=image_binary, filename="image.png")
    await ctx.channel.send("Look what I this dumbass said",file=finalImageFile)
  await ctx.message.delete()
  
def getDisplayName(author):
  if not author.nick == None:
    return author.nick
  return author.name

async def get_avatar_image_as_bytes(avatar_image):
  return await avatar_image.read()

def createFramedImage(username, byte_avatar_image, text, time="Yesterday at 9:20pm"):
  imageCanvas = Image.open("../assets/DiscordBackground.png", "r") 

  pfp = Image.open(io.BytesIO(byte_avatar_image))

  pfp = pfp.resize((150,150))

  pfpBoarder = Image.open("../assets/DiscordBlackPFPBoarder.png", "r")
  pfpBoarder.resize((150,150))

  # main text
  mainText = Image.new("RGB", (800, 200), (54, 57, 63))
  mainTextFont = ImageFont.truetype("../assets/whitneylight.otf", 55)
  mainDraw = ImageDraw.Draw(mainText)

  mainDraw.text((0,0), text, fill=(255,255,255), font=mainTextFont)

  # Name text
  nameText = Image.new("RGB", (800, 70), (54, 57, 63))
  nameTextFont = ImageFont.truetype("../assets/whitneymedium.otf", 55)
  nameDraw = ImageDraw.Draw(nameText)

  nameDraw.text((0,0), username, fill=(210,210,212), font=nameTextFont)

  #Time Text
  timeText = Image.new("RGB", (800, 70), (54, 57, 63))
  timeTextFont = ImageFont.truetype("../assets/whitneylight.otf", 42)
  timeDraw = ImageDraw.Draw(timeText)

  timeDraw.text((0,0), time, fill=(145,149,155), font=timeTextFont)

  # Merges all the images
  imageCanvas.paste(pfp,(80,75))
  imageCanvas.paste(pfpBoarder, (80,75), pfpBoarder)
  imageCanvas.paste(nameText, (270, 80))
  # makes sure time is infront of 
  imageCanvas.paste(timeText, (285+int(nameDraw.textlength(username, font=nameTextFont)), 94))
  imageCanvas.paste(mainText, (270, 157))

  return imageCanvas

