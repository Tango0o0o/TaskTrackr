import googletrans
import discord
from discord.ext import commands
from discord import OptionChoice, SelectOption

translator = googletrans.Translator()

lang_list = []

for lang in googletrans.LANGCODES.keys():
    lang_list.append(SelectOption(label=lang,value=lang))


class Translate(commands.Cog):

    def __init__(self,client) -> None:
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is ready!")
      #  await self.client.tree.add_command(InstagramGroup(name="instagram",description="commands for instagram"))
    
    @commands.slash_command(name="translate")
    async def translate(self,inter:discord.Interaction,text:str,to_language:str,from_language:str=None):
        await inter.response.send_message("Translating...")

        if from_language == None:
            from_language = translator.detect(text=text).lang
        else:
            from_language = googletrans.LANGCODES[from_language]


        translated_text = translator.translate(text=text,dest=googletrans.LANGCODES[to_language.value],src=from_language)

        embed = discord.Embed(colour=discord.Colour.random(),title="Translation")

        embed.add_field(name=f"{googletrans.LANGUAGES[from_language].capitalize()}",value=text)
        embed.add_field(name=f"{to_language.value.capitalize()}",value=translated_text)

        await inter.channel.send(embed=embed)

    @commands.slash_command()
    async def translate(self,ctx,text:str,to_language):
       # await inter.response.send_message("Translating...")
        print(1)
        translated_text = translator.translate(text=text,dest=googletrans.LANGCODES[to_language],src="english")
        print(2)
        embed = discord.Embed(colour=discord.Colour.random(),title="Translation")
        print(3)
        embed.add_field(name=f"English",value=text,inline=False )
        print(4)
        embed.add_field(name=f"{to_language.capitalize()}",value=translated_text.text,inline=False)

        await ctx.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_message(self,msg:discord.Message):
        if str(msg.author.id) == str(self.client.user.id):
            return
        
        embed = discord.Embed(colour=discord.Color.blurple(),title=f"{msg.author.name}'s message", description="Spanish to English")
        embed.add_field(name="Spanish", value=msg.content)
        embed.add_field(name="English", value=translator.translate(text=msg.content,dest=googletrans.LANGCODES["english"]).text, inline=False)
        embed.set_footer(text="Created by Walanyo")
        await msg.channel.send(embed=embed)


    


def setup(client):
    client.add_cog(Translate(client))