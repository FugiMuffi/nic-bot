import discord
import random
import re

client = discord.Client()

# add user ids for forceNick here
forceNick = {
    # id: nick,
    000000000000000000: 'qwerty',
}

# add admin user ids here
admin = {
    111111111111111111,
}


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # admin functions
    if message.author.id in admin:
        # manual nick
        # type in any text channel: $nick id nickname
        m = re.search('(\\$nick) ([0-9]*) (.*)', message.content)
        if m:
            member_id = int(m[2])
            nick = m[3]
            member = discord.utils.get(message.guild.members, id=member_id)
            if member:
                try:
                    await member.edit(nick=nick)
                    print(f'edited nick of {member_id}: {nick}')
                except discord.DiscordException as e:
                    print('error: ' + str(e.__class__))
            else:
                print('member not found')


@client.event
async def on_member_update(before, after):
    # if a user changes his nickname, change it back
    if after.id in forceNick:
        if forceNick[after.id] not in after.display_name:
            nick = forceNick[after.id]
            try:
                await after.edit(nick=nick)
                print(f'edited nick of {after.id}: {nick}')
            except discord.DiscordException as e:
                print('error: ' + str(e.__class__))


# your bot token from https://discord.com/developers/applications
client.run('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
