import discord
from dotenv import load_dotenv
import os
from Classes.client import MyClient

load_dotenv()


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv('BOT_TOKEN'))


