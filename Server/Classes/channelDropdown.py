from discord import ui, Interaction, ChannelType


class Dropdown(ui.ChannelSelect):
    def __init__(self, client, *args, **kwargs):
        self.client = client
        super(Dropdown, self).__init__(*args, **kwargs)

    async def callback(self, interaction: Interaction):
        
        selectedChannelID = self.values[0].id
        guildID = self.values[0].guild_id

        # Update the clients saved channels 
        await self.client.updateChannels(guildID, selectedChannelID)

        # Send possible text channel object here
        await interaction.response.send_message(f'The new channel is #{self.values[0]}')


class DropdownView(ui.View):
    def __init__(self, client):
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(Dropdown(client=client, placeholder='Select the channel here', min_values=1, max_values=1, channel_types=[ChannelType.text]))