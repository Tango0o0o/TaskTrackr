import discord
from discord.ui.item import Item

class food(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=10)

    async def on_timeout(self) -> None:
        self.disable_all_items()
        await self.message.edit(content="Took too long to choose!", view=self)

    @discord.ui.select(
        select_type=discord.ComponentType.user_select,
    )
    async def food(self, select, inter:discord.interactions.Interaction):
        await inter.respond(f"Interesting choice nigga... {select.values[0].mention} is ok ig...")
        self.disable_all_items()
        await inter.message.edit(content="Don't be greedy!", view=self)