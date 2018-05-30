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
    if not message.author.bot:
        args = message.content.lower().split(' ')
        await commands.discord_commands(args, client, message)
        await commands.both_commands(args, client, message)
    elif message.author.bot:
        message.author.name = message.content.lower().split(' ')[0][1:-2]
        in_game_args = message.content.lower().split(' ')[1:]
        await commands.minecraft_commands(in_game_args, client, message)
        await commands.both_commands(in_game_args, client, message)

client.run(secret_reader.read_token())
