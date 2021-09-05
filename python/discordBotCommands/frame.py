import io

from discordSimplified import find_guild_member_from_mention
from discord import File
from PIL import Image

async def _frame(bot, ctx, args):
  userToFrame = await find_guild_member_from_mention(ctx.guild, args)

  print(userToFrame.avatar_url)

  framedByteImage = createFramedImage()
  finalImageFile = File(framedByteImage, filename="epic.png")
  await ctx.channel.send(file=finalImageFile)
  
def createFramedImage():
  imageCanvas = Image.open("../assets/DiscordBackground.png", "r")
  pfp = Image.open("../assets/TemplateAvatar.png", "r")
  pfp = pfp.resize((100,100))
  imageCanvas.paste(pfp,(100,100))
  #imageByteArray = imageObjToByteArray(imageCanvas)
  
  img_byte_arr = io.BytesIO()
  imageCanvas.save(img_byte_arr, 'PNG')
  print(img_byte_arr)
  return img_byte_arr

# def imageObjToByteArray(image_obj):
#   img_byte_arr = io.BytesIO()
#   image_obj.save(img_byte_arr, format='PNG')
#   return img_byte_arr.getvalue()
