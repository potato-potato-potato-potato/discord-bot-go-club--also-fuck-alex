async def find_guild_member_from_mention(guild, opponent_mention):
  guild_members = guild.fetch_members()
  async for member in guild_members:
    mentionString = member.mention
    if cleanMention(mentionString) == cleanMention(opponent_mention):
      return member
    
      
def cleanMention(mention):
  return mention.replace("!","")