import asyncio


async def task_runs(client):
    while True:
        await asyncio.sleep(7200)
        await client.send_message(client.get_channel('442053138921553937'),
                                  '&5Join the discord server: https://discord.gg/UBCqM8y')
