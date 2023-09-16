import discord
from dotenv import load_dotenv
import os

load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        print("Message received")
        if message.author == self.user:
            print("Message from bot")
            return

        if message.content == 'ping':
            await message.channel.send('pong')
            return

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(os.getenv('BOT_TOKEN'))