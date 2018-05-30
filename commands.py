import requests

help_dict = {}
minecraft_commands_dict = {}
discord_commands_dict = {}
both_commands_dict = {}

def decorator_base(func2=None, dict={}, help=""):
    if func2 is None:
        def retval(func):
            dict[func.__name__] = func
            help_dict[func.__name__] = help
            return func
        return retval
    else:
        dict[func2.__name__] = func2
        help_dict[func2.__name__] = help
        return func2


def minecraft_only(func=None, help=""):
    return decorator_base(func, minecraft_commands_dict, help=help)

def discord_only(func=None, help=""):
    return decorator_base(func, discord_commands_dict, help=help)

def both(func=None, help=""):
    return decorator_base(func, both_commands_dict, help=help)

async def discord_commands(args, client, message):
    if args[0][1:] in discord_commands_dict.keys():
        await discord_commands_dict[args[0][1:]](args, client, message)

async def minecraft_commands(args, client, message):
    if args[0][1:] in minecraft_commands_dict.keys():
        await minecraft_commands_dict[args[0][1:]](args, client, message)

async def both_commands(args, client, message):
    if args[0][1:] in both_commands_dict.keys():
        await both_commands_dict[args[0][1:]](args, client, message)

@both
async def discord(args, client, message):
    await client.send_message(message.channel, "Join the discord: https://discord.gg/UBCqM8y")

@discord_only
async def log(args, client, message):
    await client.send_message(
        message.channel,
        "Thanks, {} your message has been logged.".format(message.author)
    )
    await client.send_message(
        client.get_channel('442476383113969664'),
        str(message.author) + ' ' + ' '.join(args[1:])
    )

@both(help="Tells you the server IPs and versions")
async def server(args, client, message):
    await client.send_message(message.channel, "MS3D: ms3d.tahgcraft.com 3.3.1.4")
    await client.send_message(message.channel, "Sevtech: sevtech.tahgcraft.com 3.0.7 - use FTBU x.14")
    await client.send_message(message.channel, "Continuum: continuum.tahgcraft.com 1.0.2")

@minecraft_only(help="n y e t  m y  l i t t l e  c y k a s")
async def giveitem(args, client, message):
    await client.send_message(message.channel, "No cheating for you!")

def commands_impl(dict):
    text = ""
    for command in list(dict.keys()):
        if help_dict[command] is "":
            text += f"    !{command}\n"
        else:
            text += f"    !{command} - {help_dict[command]}\n"
    text += "\n"
    return text

@both(help="This command list")
async def commands(args, client, message):
    text = "```\n"

    text += "Commands for discord and minecraft" + "\n"
    text += commands_impl(both_commands_dict)

    text += "Commands for only discord" + "\n"
    text += commands_impl(discord_commands_dict)

    text += "Commands for only minecraft" + "\n"
    text += commands_impl(minecraft_commands_dict)

    text += "```"

    await client.send_message(message.channel, text)

@both(help="This command list")
async def help(args, client, message):
    await commands(args, client, message)

@both
async def begfordw20(args, client, message):
    await client.send_message(message.channel, "FOR THE LAST TIME! IT'S NOT UP TO ME!")

@minecraft_only
async def add(args, client, message):
    await client.send_message(message.channel, float(args[1]) + float(args[2]))

@minecraft_only
async def multiply(args, client, message):
    await client.send_message(message.channel, float(args[1]) * float(args[2]))

@minecraft_only
async def subtract(args, client, message):
    await client.send_message(message.channel, float(args[1]) - float(args[2]))

@minecraft_only
async def divide(args, client, message):
    await client.send_message(message.channel, float(args[1]) / float(args[2]))

@both(help="First argument is the question, the rest are the choices")
async def poll(args, client, message):
    question = args[0]
    answers = args[1:]
    data = {
        "title": question,
        "options": answers
    }
    new_poll_request = requests.post("https://www.strawpoll.me/api/v2/polls", json=data)
    print(new_poll_request.text)
    poll_url = f"https://strawpoll.me/{new_poll_request.json()['id']}"
    message_txt = f"Created New Poll!\n{question}\n{poll_url}"
    await client.send_message(message.channel, message_txt)
