import json

async def StoreDiscordChannelInvite(guild):
  textChannel = await getTextChannel(guild)
  invite = await textChannel.create_invite(max_age = 0, max_uses = 0, reason = "For managing internal processes")
  invite_url = invite.url
  await storeInvite(guild, invite_url)

async def getTextChannel(guild):
  textChannels = guild.text_channels
  return textChannels[0]

guildInfo = 'DataDefinitlyNotStolen/guildInfo.json'
async def storeInvite(guild, invite_url):
  data = None
  #Takes in file data and saves it, as well as appends new data
  with open(guildInfo) as json_file:
    data = json.load(json_file)
    dataAlreadyContainsGuild = False
    for invite_obj in data['invite_urls']:
      if invite_obj['guildID'] == guild.id:
        dataAlreadyContainsGuild = True

    if not dataAlreadyContainsGuild:
      data['invite_urls'].append({
        "guildName": guild.name,
        "guildID": guild.id,
        "url": invite_url
      })

  # Pushs changes to the file
  with open(guildInfo, 'w') as json_file:
    json.dump(data, json_file)
