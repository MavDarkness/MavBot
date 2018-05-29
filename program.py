import discord
import taskruns
import secrets

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print('Discord version number: {}'.format(discord.__version__))
    await taskruns.task_runs()


@client.event
async def on_message(message):
    print(message.author)

    if message.author != client.get_user_info('446091547637710859'):
        args = message.content.lower().split(' ')

        if args[0] == '!log':
            await client.send_message(message.channel,
                                      "Thanks, {} your message has been logged.".format(message.author))
            await client.send_message(client.get_channel('442476383113969664'),
                                      str(message.author) + ' ' + ' '.join(args[1:]))
    elif message.author == user.bot:
        print(message.content)

client.run(secrets.token())
