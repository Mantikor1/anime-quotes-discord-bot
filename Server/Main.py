import discord
from dotenv import load_dotenv
import os
from Classes.client import MyClient

load_dotenv()

# Give the bot the default permissions, this could get optimized in the future
intents = discord.Intents.default()
intents.message_content = True

# Create the main class and run the bot
client = MyClient(intents=intents, channelID=os.getenv('CHANNEL_ID'))
client.run(os.getenv('BOT_TOKEN'))


