import discord
from discord.ext import tasks
from datetime import datetime
from Classes.question import Question

class MyClient(discord.Client):

    def __init__(self, *args, **kwargs):

        # This should rather be a file or database entry to make it restart consistent
        self.channelIDs = []
        self.question = Question()
        #self.channelID = kwargs['channelID'] # Get the channel ID from the .env file

        super(MyClient, self).__init__(*args, **kwargs)


    async def on_ready(self):
        print('Logged on as', self.user)

        # send inital question
        # await self.sendQuestion(self.channelIDs)


    async def updateChannels(self, guildID, channelID):
        
        for object in self.channelIDs:
            if object["guildID"] == guildID:
                # Existing guild found to update
                object["channelID"] = channelID
                print(f'Updated existing guild channel: {channelID}')
                await self.sendQuestion(self.channelIDs)
                return
        
        # New guild with new channel
        self.channelIDs.append({"guildID": guildID, "channelID": channelID})
        print(f'Added new channel {channelID} for guild {guildID}')
        await self.sendQuestion(self.channelIDs)


    # Creates a loop than checks the time every 1 second
    @tasks.loop(seconds=1)
    async def checkTime(self):
        currentTime = datetime.now()
        if currentTime.hour == 0 and currentTime.minute == 0 and currentTime.second == 0:
            await self.sendQuestion()


    async def sendQuestion(self, channelIDs):
        for channel in channelIDs:
            channelObject = self.get_channel(int(channel["channelID"]))
            if channelObject:
                await channelObject.send('Guess the anime and character by the following quote: \n"' + self.question.quote + '"')
            else:
                print(f"Channel {channel['channelID']} on guild {channel['guildID']} doesn't exist")


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
            
        else:
            await message.channel.send("Keep on guessing lol!")

        await message.channel.send("bot still replies to messages")
        if message.content == 'ping':
            await message.channel.send('pong')
        return
    
    