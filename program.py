import discord
import taskruns
import secret_reader
import commands

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
<<<<<<< HEAD
        args = message.content.lower().split(' ')

        if args[0] == '!log':
            await client.send_message(message.channel,
                                      "Thanks, {} your message has been logged.".format(message.author))
            await client.send_message(client.get_channel('442476383113969664'),
                                      str(message.author) + ' ' + ' '.join(args[1:]))
=======
    if not message.author.bot:
        args = message.content.lower().split(' ')
        await commands.discord_commands(args, client, message)
        await commands.both_commands(args, client, message)
    elif message.author.bot:
        message.author.name = message.content.lower().split(' ')[0][1:-2]
        in_game_args = message.content.lower().split(' ')[1:]
        await commands.minecraft_commands(in_game_args, client, message)
        await commands.both_commands(in_game_args, client, message)
>>>>>>> upstream/master

client.run(secret_reader.read_token())
