from os import getenv
from discord import Intents, app_commands, Interaction
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
@tree.command(name="settings", description="You can set the channel for the bot to post the quiz questions here!")
async def commandSettings(interaction: Interaction):
    await interaction.response.send_message('Please select the target channel for the quiz: ', view=DropdownView(client), ephemeral=True)


@tree.command(name="anime", description="Guess the title of the anime!")
async def commandAnimeTitle(interaction: Interaction, title: str):
    await interaction.response.send_message(client.answerQuestion("title", title, interaction.user.display_name), ephemeral=False)

@tree.command(name="character", description="Guess the character!")
async def commandAnimeTitle(interaction: Interaction, character: str):
    await interaction.response.send_message(client.answerQuestion("character", character, interaction.user.display_name), ephemeral=False)

@client.event
# remove the guild together with the channel from the list and csv file, when removed from a guild
async def on_guild_remove(guild):
    client.removeGuild(str(guild.id))
    print("Bot has been removed from a guild!")

# Only comment this in, when you made changes to the commands
# @client.event
# async def on_ready():
#     print('Logged on as', client.user)  
#     await tree.sync()
#     print('Synced')

token = getenv("BOT_TOKEN")
client.run(token)


