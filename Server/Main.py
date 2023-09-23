import discord
from discord.ext import tasks
from dotenv import load_dotenv
import os
from datetime import datetime
import json

dir = os.path.dirname(__file__)
file = open(dir + "\\quotes.json")
quotes = json.load(file)
# quotes = [{
#     "quote": "The world isn’t perfect. But it’s there for us, doing the best it can… that’s what makes it so damn beautiful.",
#     "character": "Roy Mustang",
#     "title": "Full Metal Alchemist"
# }]

load_dotenv()

class Question():
    def __init__(self):
        questions = self.drawQuote()
        self.quote = questions["quote"]
        self.title = questions["title"]
        self.character = questions["character"]
        self.titleFound = False
        self.characterFound = False

    def drawQuote(self):
        return quotes[1]

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        self.channel = None
        self.question = Question()
        super(MyClient, self).__init__(*args, **kwargs)

    async def on_ready(self):
        print('Logged on as', self.user)

        # Start the coroutine
        self.checkTime.start()

        channel = self.get_channel(1080108766629990410)
        if channel:
            self.channel = channel

        # send inital question
        await self.sendQuestion()

    @tasks.loop(seconds=1)
    async def checkTime(self):
        currentTime = datetime.now()
        if currentTime.hour == 0 and currentTime.minute == 0 and currentTime.second == 0:
            await self.sendQuestion()

    async def on_message(self, message):
        # don't respond to ourselves
        #print("Message received")
        if message.author == self.user:
            #print("Message from bot")
            return

        if message.content == self.question.title:
            if self.question.titleFound == True:
                await message.channel.send("Title has already been found...")
            await message.channel.send("You found the correct anime title: " + self.question.title)
            self.question.titleFound = True

        elif message.content == self.question.character:
            if self.question.characterFound == True:
                await message.channel.send("Character has already been found...")
            await message.channel.send("You found the correct character: " + self.question.character)
            self.question.characterFound = True
        else:
            await message.channel.send("Keep on guessing lol!")

        #await message.channel.send("bot still replies to messages")
        # if message.content == 'ping':
        #     await message.channel.send('pong')
        #return
    
    async def sendQuestion(self):
        await self.channel.send('Who said this quote in which anime? \n"' + self.question.quote + '"')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv('BOT_TOKEN'))


