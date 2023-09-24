import discord
from discord.ext import tasks
from datetime import datetime
from Classes.question import Question

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        self.channel = None
        self.question = Question()
        self.channelID = kwargs['channelID'] # Get the channel ID from the .env file
        super(MyClient, self).__init__(*args, **kwargs)

    async def on_ready(self):
        print('Logged on as', self.user)

        # Start the coroutine
        self.checkTime.start()

        # Get the channel
        channel = self.get_channel(int(self.channelID))
        if channel:
            self.channel = channel

        # send inital question
        await self.sendQuestion()

    # Creates a loop than checks the time every 1 second
    @tasks.loop(seconds=1)
    async def checkTime(self):
        currentTime = datetime.now()
        if currentTime.hour == 0 and currentTime.minute == 0 and currentTime.second == 0:
            await self.sendQuestion()

    async def on_message(self, message):

        # don't respond to ourselves
        if message.author == self.user:
            return

        # Check the message content
        if message.content == "!"+self.question.title:
            if self.question.titleFound == True:
                await message.channel.send("Title has already been guessed...")
            await message.channel.send("You found the correct anime title: " + self.question.title)
            self.question.titleFound = True # Set to true for the correct answer so it can't get answered multiple times

        elif message.content == "!"+self.question.character:
            if self.question.characterFound == True:
                await message.channel.send("Character has already been guessed...")
            await message.channel.send("You found the correct character: " + self.question.character)
            self.question.characterFound = True
            
        # else:
        #     await message.channel.send("Keep on guessing lol!")

        #await message.channel.send("bot still replies to messages")
        # if message.content == 'ping':
        #     await message.channel.send('pong')
        #return
    
    async def sendQuestion(self):
        await self.channel.send('Who said this quote in which anime? \n"' + self.question.quote + '"')