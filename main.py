import discord
import os
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    question = message.content.lower().strip()

    if question == '!hi':
        await message.channel.send(f'hello 💕👋🏻')

    elif question == '!gcollab':
        await message.channel.send(
            'Visit the analysis process in google collab\n'
            f'https://colab.research.google.com/drive/1qr9LXDj-E9btf-olzvyc-NzYFmNo9osI?usp=sharing')

    elif ("top" and "countries") in question or "popular countries" in question:
        await message.channel.send(
            "**Top 5 countries by number of titles**\n"
            "1. United States\n"
            "2. India\n"
            "3. Unknown\n"
            "4. United Kingdom\n"
            "5. Canada"
        )
        await message.channel.send(file=discord.File("download (2).png"))

    elif ("rating" and "distribution") in question or "ratings" in question:
        await message.channel.send(
            "**Netflix rating Distribution**\n"
        )
        await message.channel.send(file=discord.File("download.png"))

    elif ("genres" and "growing") in question  or ("genre" and "trend") in question or ("genres" and "growth") in question:
        await message.channel.send(
            "**Genre Growth Over Time**\n"
        )

        await message.channel.send(file=discord.File("download (3).png"))

    elif "longest movies" in question or "movie duration" in question:
        await message.channel.send(
            "**Countries with the Longest Average Movies**\n"
        )
        await message.channel.send(file=discord.File("download (4).png"))

    elif "genres" in question or "popular genres" in question:
        await message.channel.send(
            "**top 5 netflix genres**\n"
            "1. International Movies\n"
            "2. Dramas \n"
            "3. Comedies\n"
            "4. International TV Shows\n"
            "5. Documentaries\n"
        )
        await message.channel.send(file=discord.File("download (1).png"))
        

    else:
        await message.channel.send(f'https://giphy.com/gifs/animation-2d-Z21HJj2kz9uBG')

@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

client.run(os.environ["DISCORD_TOKEN"])