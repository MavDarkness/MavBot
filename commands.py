import requests

minecraft_commands_dict = {}
discord_commands_dict = {}
both_commands_dict = {}

def minecraft_only(func):
    minecraft_commands_dict[func.__name__] = func
    return func

def discord_only(func):
    discord_commands_dict[func.__name__] = func
    return func

def both(func):
    both_commands_dict[func.__name__] = func
    return func

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

@both
async def server(args, client, message):
    await client.send_message(message.channel, "MS3D: ms3d.tahgcraft.com 3.3.1.4")
    await client.send_message(message.channel, "Sevtech: sevtech.tahgcraft.com 3.0.7 - use FTBU x.14")
    await client.send_message(message.channel, "Continuum: continuum.tahgcraft.com 1.0.2")

@minecraft_only
async def giveitem(args, client, message):
    await client.send_message(message.channel, "No cheating for you!")

@both
async def commands(args, client, message):
    text = "```\n"

    text += "Commands for discord and minecraft" + "\n"
    for command in list(both_commands_dict.keys()):
        text += "    !" + command + "\n"
    text += "\n"

    text += "Commands for only discord" + "\n"
    for command in list(discord_commands_dict.keys()):
        text += "    !" + command + "\n"
    text += "\n"

    text += "Commands for only minecraft" + "\n"
    for command in list(minecraft_commands_dict.keys()):
        text += "    !" + command + "\n"

    text += "```"

    await client.send_message(message.channel, text)



@both
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

@both
async def output(args, client, message):
    for i in range(len(args)):
        print(i, args[i])

@both
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
