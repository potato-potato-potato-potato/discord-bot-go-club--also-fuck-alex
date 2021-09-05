import random
from discordSimplified import find_guild_member_from_mention

async def _banFlip(ctx, opponent_mention):
  invoked_player = ctx.author
  opponent_player = await find_guild_member_from_mention(ctx.guild, opponent_mention) 

  if random.randint(0, 1) == 1:
    await ctx.channel.send(opponent_player.mention + " gets banned!")
  else:
    await ctx.channel.send(invoked_player.mention + " gets banned!")