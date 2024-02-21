import discord
from discord.ext import commands
from random import randint
import json

class CharacterActions(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    actions = discord.SlashCommandGroup(name="actions", description="Actions which your characters can do")
    gamble = actions.create_subgroup(name="gamble")

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is ready!")
    
    @gamble.command(name="guess-number", description="Guess 3 numbers between 1 and 500 to get some money!")
    async def guess_number(self, ctx:discord.ApplicationContext, guess1:int, guess2:int, guess3: int):
        await ctx.defer()

        if guess1 + guess2 + guess3 > 1500 or guess1 + guess2 + guess3 < 0:
            await ctx.respond("Invalid guesses")
            return

        with open("Todo\Discord\Python Files\Cogs\Character\Data.json", "r") as file:
            data = json.load(file)

        character = data[str(ctx.author.id)]["Selected"]
        num1 = randint(1, 500)
        num2 = randint(1, 500)
        num3 = randint(1, 500)
        dif1 = abs(num1-guess1)
        dif2 = abs(num2-guess2)
        dif3 = abs(num3-guess3)

        total = randint(350, 500) - (dif1+dif2+dif3)
        data[str(ctx.author.id)]["Characters"][character]["Money"]["Bank"] += total

        if total < 0:
            totalembed = discord.EmbedField(name="Loss", value=f"You lost £{abs(total)}", inline=False)
        elif total > 0:
            totalembed = discord.EmbedField(name="Profit", value=f"You made £{abs(total)}", inline=False)
        else:
            totalembed = discord.EmbedField(name="Nothing!?", value=f"You made nothing!", inline=False)

        embed = discord.Embed(
            colour=discord.Colour.gold(),
            title="🤑🤑🤑",
            fields=[
                discord.EmbedField(name="Guess 1", value=f"You were {dif1} away.", inline=False),
                discord.EmbedField(name="Guess 2", value=f"You were {dif2} away.", inline=False),
                discord.EmbedField(name="Guess 3", value=f"You were {dif3} away.", inline=False),
                totalembed,
            ],
            footer=discord.EmbedFooter(text=f"Playing as {character}") 
        )

        with open("Todo\Discord\Python Files\Cogs\Character\Data.json", "w") as file:
            json.dump(data, file, indent=4)

        await ctx.respond(embed=embed,ephemeral=True)
        
    

def setup(bot):
    bot.add_cog(CharacterActions(bot))