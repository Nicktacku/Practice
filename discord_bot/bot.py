import discord
from responses import get_response
from discord.ext import commands, tasks
import datetime as dt
import asyncio
from news_summarizer import get_news


async def send_message(message, user_message, is_private):
    try:
        response = get_response(user_message)
        await message.author.send(
            response
        ) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = "ODc0NTIyNzc2NzgwODMyNzc4.GNOr8V.2Py54CfOnX83fbzcvTdWS9mAfwIABohmHz3TU8"

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running")
        msg1.start()

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return ()

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said {user_message} in {channel}")

        if user_message[0] == "?":
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    @tasks.loop(hours=8)
    async def msg1():
        user = await client.fetch_user("nicktacku")
        news = get_news()
        await user.send(f"**Title:** {news[0]}\n**Date:** {news[1]}\n\n{news[2]}")

    client.run(TOKEN)
