from typing import Any
import discord
from discord.ext import commands, tasks
from discord.flags import Intents
from dotenv import load_dotenv
import os
import sys
from datetime import datetime
import threading
from time import sleep
import asyncio


load_dotenv()



class MyClient(discord.Client):
    def __init_subclass__(self) -> None:
        self.channel = None
        return super().__init_subclass__()

    async def on_ready(self):
        print('Logged on as', self.user)

        # Start the coroutine
        self.checkTime.start()

        channel = self.get_channel(1080108766629990410)
        if channel:
            self.channel = channel

    @tasks.loop(seconds=1)
    async def checkTime(self):
        currentTime = datetime.now()
        if currentTime.minute == 27 and currentTime.second == 0:
            await self.sendQuestion()

    async def on_message(self, message):
        # don't respond to ourselves
        print("Message received")
        if message.author == self.user:
            print("Message from bot")
            return

        await message.channel.send("bot still replies to messages")
        # if message.content == 'ping':
        #     await message.channel.send('pong')
        return
    
    async def sendQuestion(self):
    # await client.wait_until_ready()
        self.channel.send("dumb bot stuck in loop")

    def printTime(self):
        while True:
            currentTime = datetime.now()
            print(currentTime.strftime("%H:%M:%S"))
            # if currentTime.minute == 27 and currentTime.second == 0:
            #     await self.sendMessage()
            sleep(1)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv('BOT_TOKEN'))


