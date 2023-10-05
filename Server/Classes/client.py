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


    '''
    Sends a question with a quote to all set channels (1 per guild)
    '''
    async def sendQuestion(self, channelIDs):

        for channel in channelIDs:
            channelObject = self.get_channel(int(channel["channelID"]))
            if channelObject:
                await channelObject.send('Guess the anime and character by the following quote: \n\n"' + self.question.quote + '"')
            else:
                print(f"Channel {channel['channelID']} on guild {channel['guildID']} doesn't exist")


    def answerQuestion(self, type, answer):

        if type == "title":
            if self.question.titleFound == True:
                return "The anime has already been guessed..."

            if answer == self.question.title:
                self.question.titleFound = True
                return f"You found the correct title! The title was {self.question.title}"
            else:
                return "Keep on guessing LOL!"

        elif type == "character":
            if self.question.characterFound == True:
                return "The character has already been guessed..."
                
            if answer == self.question.character:
                self.question.characterFound = True
                return f"You found the correct title! The title was {self.question.character}"
            else:
                return "Keep on guessing LOL!"

    
    