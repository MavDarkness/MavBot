import discord
import asyncio

client = discord.Client()


async def task_runs():
    while True:
        await asyncio.sleep(7200)
        await client.send_message(
            client.get_channel('442053138921553937'), '&5Join the discord server: https://discord.gg/UBCqM8y')

