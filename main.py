import os
from dotenv import load_dotenv

from discord import Intents, Client, Message
from responses import get_response

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True  
client = Client(intents=intents)


async def send_message(message: Message, user_message):
    await get_response(message)

@client.event
async def on_ready():
    print(f'{client.user} is now running')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username = str(message.author)
    user_message = message.content
    channel = str(message.channel)

    print(f'[{channel,}] {username}:{user_message}')
    await send_message(message, user_message)


def main():
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()

