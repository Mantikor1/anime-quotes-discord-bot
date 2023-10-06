import os
from discord import Intents, app_commands, Interaction, Object
from dotenv import load_dotenv
from Classes.client import MyClient
from Classes.channelDropdown import DropdownView

load_dotenv()


# Give the bot the default permissions, this could get optimized in the future
intents = Intents.default()
intents.message_content = True

# Create the main class and run the bot
client = MyClient(intents=intents, command_prefix="/")
tree = app_commands.CommandTree(client)

### Registered commands
@tree.command(name="settings", description="You can set the channel for the bot to post the quiz questions here!", guild=Object(id=949628705553137684))
async def commandSettings(interaction: Interaction):
    await interaction.response.send_message('Please select the target channel for the quiz: ', view=DropdownView(client), ephemeral=True)

@tree.command(name="anime", description="Guess the title of the anime!", guild=Object(id=949628705553137684))
async def commandAnimeTitle(interaction: Interaction, title: str):
    await interaction.response.send_message(client.answerQuestion("title", title))

@tree.command(name="character", description="Guess the character!", guild=Object(id=949628705553137684))
async def commandAnimeTitle(interaction: Interaction, character: str):
    await interaction.response.send_message(client.answerQuestion("character", character))

# # Only comment this in, when you made changes to the commands
# @client.event
# async def on_ready():
#     print('Logged on as', client.user)  
#     await tree.sync(guild=Object(id=949628705553137684))
#     print('Synced')

token = os.getenv("BOT_TOKEN")
client.run(token)


