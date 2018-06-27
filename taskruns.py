import time


async def task_runs(client):
    test = True
    while test:
        # await time.sleep(7200)
        await client.send_message(client.get_channel('442053138921553937'),
                                  'Join the discord server: https://discord.gg/UBCqM8y')
        test = False
