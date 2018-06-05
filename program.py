import discord
import taskruns
import secret_reader
import commands
import re

client = discord.Client()

in_game_msg_regex = re.compile(r"<([a-zA-Z0-9]+)>: (.*)")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print('Discord version number: {}'.format(discord.__version__))
    await taskruns.task_runs()


def process_args(arg_str):
    split = arg_str.split(" ")
    in_str = False
    args = []
    for word in split:
        if len(word) == 0:
            # If there are multiple spaces between words
            continue
        elif in_str:
            # If we are currently between quotes
            if word[-1] == "\"":
                # If the word ends with a quote
                in_str = False
                args[-1] += word[:-1]
            else:
                # If the word is just text
                args[-1] += word + " "
        else:
            if word[0] == "\"":
                # If the word starts with a quote
                if len(word) == 1:
                    # If the word is a single quote with no text
                    args.append("\"")
                else:
                    if word[-1] == "\"" and not word[-2] == "\\":
                        # If the word ends with a quote
                        if not len(word) == 2:
                            # If the word is more than just two quotes
                            args.append(word[1:-1])
                    else:
                        # If the word is like "text
                        in_str = True
                        args.append(word[1:] + " ")
            else:  # If there are no quotes to deal with
                args.append(word)
    # Replace \" with ", in case you actually need to type a quote
    return [arg.replace("\\\"", "\"") for arg in args]


@client.event
async def on_message(message):
    if message.author.bot:
        msg_match = in_game_msg_regex.match(message.content)
        if msg_match is None:
            # This would be if a bot said something besides echoing from MC
            pass
        else:
            # This would be if a bot said something that was echoed from MC
            message.author.name = msg_match.group(1)
            args = process_args(msg_match.group(2))
            await commands.minecraft_commands(args, client, message)
            await commands.both_commands(args, client, message)
    else:
        args = process_args(message.content)
        await commands.discord_commands(args, client, message)
        await commands.both_commands(args, client, message)

if __name__ == "__main__":
    client.run(secret_reader.read_token())
