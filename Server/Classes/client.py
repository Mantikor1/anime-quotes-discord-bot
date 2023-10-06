import discord
from discord.ext import tasks
from datetime import datetime
import csv
from Classes.question import Question
import os

class MyClient(discord.Client):

    def __init__(self, *args, **kwargs):

        self.channelIDs = []

        with open(os.path.dirname(__file__) + '/../Data/channels.csv', "r", newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=' ')
            for row in csvreader:
                if row:
                    channel = {"guildID": row[0], "channelID": row[1]}
                    self.channelIDs.append(channel)
                else:
                    print("ChannelID file is empty")

        # print(self.channelIDs)
        
        self.question = Question()

        super(MyClient, self).__init__(*args, **kwargs)


    async def on_ready(self):
        print('Logged on as', self.user)

        # send inital question
        # await self.sendQuestion(self.channelIDs)

    def updateChannelFile(self, channelList):
        with open(os.path.dirname(__file__) + '/../Data/channels.csv', "w", newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=' ')
            for channel in channelList:
                csvwriter.writerow([channel["guildID"], channel["channelID"]])

    async def updateChannels(self, guildID, channelID):
        
        for object in self.channelIDs:
            if object["guildID"] == guildID:
                # Existing guild found to update
                object["channelID"] = channelID
                self.updateChannelFile(self.channelIDs)
                print(f'Updated existing guild channel: {channelID}')
                await self.sendQuestion(self.channelIDs)
                return
        
        # New guild with new channel
        self.channelIDs.append({"guildID": guildID, "channelID": channelID})
        self.updateChannelFile(self.channelIDs)
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

    
    