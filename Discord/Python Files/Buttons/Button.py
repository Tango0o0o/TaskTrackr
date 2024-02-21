import discord
import Modals


class hi(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None) # timeout of the view must be set to None

    @discord.ui.button(label="Say hi!",custom_id="hi", style=discord.ButtonStyle.green, emoji="👋", row=0)
    async def button_callback(self, button, inter:discord.interactions.Interaction):
        await inter.respond("Thanks for saying hi!")
    
    @discord.ui.button(label="Say wsg!",custom_id="wsg", style=discord.ButtonStyle.red, emoji="😐", row=1)
    async def button_callback1(self, button, inter:discord.interactions.Interaction):
        await inter.respond("Your not bad")
