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

@tree.command(name="settings", description="this is a test command", guild=Object(id=949628705553137684))
async def testcommand(interaction: Interaction):
    await interaction.response.send_message('Please select the target channel for the quiz: ', view=DropdownView(client))
    await tree.sync(guild=Object(id=949628705553137684))

token = os.getenv("BOT_TOKEN")
client.run(token)


