import io

from discordSimplified import find_guild_member_from_mention
from discord import File
from PIL import Image

async def _frame(bot, ctx, args):
  userToFrame = await find_guild_member_from_mention(ctx.guild, args)

  print(userToFrame.avatar_url)

  framedImage = createFramedImage()
  
  with io.BytesIO() as image_binary:
    framedImage.save(image_binary, "PNG")
    image_binary.seek(0)
    finalImageFile = File(fp=image_binary, filename="image.png")
    await ctx.channel.send(file=finalImageFile)
  
def createFramedImage():
  imageCanvas = Image.open("../assets/DiscordBackground.png", "r")
  pfp = Image.open("../assets/TemplateAvatar.png", "r")
  pfp = pfp.resize((150,150))

  pfpBoarder = Image.open("../assets/DiscordBlackPFPBoarder.jpg", "r")
  pfpBoarder.resize((150,150))

  imageCanvas.paste(pfp,(100,100))
  imageCanvas.paste(pfpBoarder, (200,100))

  return imageCanvas

