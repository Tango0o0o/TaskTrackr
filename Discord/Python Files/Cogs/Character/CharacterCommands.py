import discord
from discord.ext import commands, bridge, pages
import json
from discord import OptionChoice, SelectOption
from discord.ui.item import Item

black = []

class select_skin(discord.ui.View):

    @discord.ui.select(
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(
                label="Black",
                emoji="👨🏿"
            ),

            discord.SelectOption(
                label="Brown",
                emoji="👨🏾"
            ),

            discord.SelectOption(
                label="Lightskin",
                emoji="👨🏽"
            ),

            discord.SelectOption(
                label="White",
                emoji="👨🏻"
            ),

             discord.SelectOption(
                label="Yellow",
                emoji="👨"
            ),

        ]
    )
    async def callback(self, select, inter:discord.Interaction):
        with open("Todo\Discord\Python Files\Cogs\Character\Data.json", "r") as file:
            data = json.load(file)

        character = data[str(inter.user.id)]["Selected"]
        data[str(inter.user.id)]["Characters"][character]["Skin color"] = select.values[0]    

        with open("Todo\Discord\Python Files\Cogs\Character\Data.json", "w") as file:
            json.dump(data, file, indent=4)


        await inter.respond("Skin color set!")

class select_gender(discord.ui.View):
    @discord.ui.select(
        min_values=1,
        max_values=1,
        options=[
            SelectOption(label="Male", emoji="♂️"),
            SelectOption(label="Female", emoji="♀️"),
        ]
    )
    async def callback1(self, select, inter:discord.Interaction):
        with open("Todo\Discord\Python Files\Cogs\Character\Data.json", "r") as file:
            data = json.load(file)

        character = data[str(inter.user.id)]["Selected"]
        data[str(inter.user.id)]["Characters"][character]["Gender"] = select.values[0]    

        with open("Todo\Discord\Python Files\Cogs\Character\Data.json", "w") as file:
            json.dump(data, file, indent=4)

        await inter.respond("Gender set!")

class CharacterCommands(commands.Cog):

    def __init__(self, bot:commands.Bot) -> None:
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is ready!")

    @commands.slash_command(name="test3")
    async def test3(self, ctx):
        await ctx.respond("test3")

    character = discord.SlashCommandGroup("character", "Commands related to your character")
    edit = character.create_subgroup("edit", "Commands to edit your character")

    @character.command(name="create", description="Create your character")
    async def create(self, ctx:discord.ApplicationContext, name:str):
        await ctx.defer()
        with open("Todo\Discord\Python Files\Cogs\Character\Data.json", "r") as file:
            data = json.load(file)

        if str(ctx.author.id) in data:
            pass
        else:
            data[str(ctx.author.id)] = {}

        if "Characters" in data[str(ctx.author.id)]:
            pass
        else:
            data[str(ctx.author.id)]["Characters"] = {}
        
        data[str(ctx.author.id)]["Selected"] = name.lower().capitalize()
        data[str(ctx.author.id)]["Characters"][name.lower().capitalize()] = {}
        data[str(ctx.author.id)]["Characters"][name.lower().capitalize()]["Money"] = {}
        data[str(ctx.author.id)]["Characters"][name.lower().capitalize()]["Money"]["Bank"] = 0
        data[str(ctx.author.id)]["Characters"][name.lower().capitalize()]["Money"]["Cash"] = 0

        with open("Todo\Discord\Python Files\Cogs\Character\Data.json", "w") as file:
            json.dump(data, file, indent=4)

        await ctx.respond(f"Character created. Please use edit commands to further create {name}.")
    
    @character.command(name="switch", description="Switch to a differenct character")
    async def switch(self, ctx:discord.ApplicationContext):
        await ctx.defer()
        with open("Todo\Discord\Python Files\Cogs\Character\Data.json", "r") as file:
            data = json.load(file)

        characters = [x for x in data[str(ctx.author.id)]["Characters"]]
        options = []
        for char in characters:
            options.append(SelectOption(label=f"{char}", emoji="🛐"))

        class switch_character(discord.ui.View):
            
            @discord.ui.select(
                min_values=1,
                max_values=1,
                options=options
            )
            async def callback1(self, select, inter:discord.Interaction):
                

                data[str(inter.user.id)]["Selected"] = select.values[0]

                with open("Todo\Discord\Python Files\Cogs\Character\Data.json", "w") as file:
                    json.dump(data, file, indent=4)

                await inter.respond(f"Swicthed to {select.values[0]}")
                select.disabled = True
                await inter.response.edit_message(view=self)
        
        await ctx.respond(view=switch_character())

    @edit.command(name="all", description="Edit all character attributes")
    async def all(self, ctx:discord.ApplicationContext):

        with open("Todo\Discord\Python Files\Cogs\Character\Data.json", "r") as file:
            data = json.load(file)

        character = data[str(ctx.author.id)]["Selected"]
        select_pages = [
            pages.Page(custom_view=select_gender(),embeds=[discord.Embed(color=discord.Colour.blurple(), title="Select Gender", footer=discord.EmbedFooter(text=f"Playing as {character}"))]),
            pages.Page(custom_view=select_skin(),embeds=[discord.Embed(color=discord.Colour.blurple(), title="Select skin colour", footer=discord.EmbedFooter(text=f"Playing as {character}"))]),
        ]
        paginator = pages.Paginator(select_pages)
        await paginator.respond(ctx.interaction, ephemeral=True)

    @character.command(name="selected", description="Check what character is selected")
    async def selected(self, ctx):
        with open("Todo\Discord\Python Files\Cogs\Character\Data.json", "r") as file:
            data = json.load(file)

        character = data[str(ctx.author.id)]["Selected"]

        await ctx.respond(character)
    
    @character.command(name="stats")
    async def stats(self,ctx:discord.ApplicationContext):
        with open("Todo\Discord\Python Files\Cogs\Character\Data.json", "r") as file:
            data = json.load(file)

        character = data[str(ctx.author.id)]["Selected"]
        embed = discord.Embed(title=f"{character}'s stats")
        embed.add_field(name="Running",value=70,inline=False)
        embed.add_field(name="Stealth",value=95,inline=False)
        embed.add_field(name="Swimming",value=22,inline=False)
        embed.add_field(name="Stamina",value=55,inline=False)
        embed.add_field(name="Speed",value=99,inline=False)
        await ctx.respond(embed=embed)        

def setup(bot):
    bot.add_cog(CharacterCommands(bot))