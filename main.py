import discord
import os
intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

def get_users_in_channel():
    channel = client.get_channel(703413308866297957)  # gets the channel you want to get the list from
    members = channel.voice_states.keys()  # finds members connected to the channel
    mem = []
    print('members: {}'.format(members))
    for member in members:
        print('client: {}'.format(client.get_user(member)))
        if client.get_user(member):
            mem.append(client.get_user(member).display_name)

    return mem

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    await client.wait_until_ready()
    if message.author == client.user:
        return

    if 'Nic' in message.content or 'nic' in message.content:
        await message.channel.send('What a cunt!')
    # if 'BetterBot' in message.content:
    #     await message.channel.send('Get it Up Ye, TAP-Bot!')

    if message.content.startswith('BetterTeam'):
        no_of_teams = 2
        if len(message.content.split(' ')[-1]) == 1:
            no_of_teams = int(message.content.split(' ')[-1])
        members = get_users_in_channel()
        splited = [members[i::no_of_teams] for i in range(no_of_teams)]
        print(splited)
        for i in range(len(splited)):
            await message.channel.send('Team {}: {}'.format(i+1, splited[i]))

client.run(os.environ['SECRET_KEY'])