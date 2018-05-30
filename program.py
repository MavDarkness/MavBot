import discord
import taskruns
import secret_reader
import commands
import re

client = discord.Client()

ingame_msg_regex = re.compile(r"<([a-zA-Z0-9]+)>: (.*)")

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
    if message.author.bot:
        msg_match = ingame_msg_regex.match(message.content.lower())
        if msg_match is None:
            # This would be if a bot said something besides echoing from MC
            pass
        else:
            # This would be if a bot said something that was echoed from MC
            message.author.name = msg_match.group(1)
            args = msg_match.group(2).split(" ")
            await commands.minecraft_commands(args, client, message)
            await commands.both_commands(args, client, message)
    else:
        args = message.content.lower().split(" ")
        await commands.discord_commands(args, client, message)
        await commands.both_commands(args, client, message)

client.run(secret_reader.read_token())
