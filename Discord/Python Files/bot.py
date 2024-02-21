import discord
from discord.ext import commands, bridge
from Menus import Menu
import os # default module
TOKEN = "MTE3MTE3Njc0MDUwOTQ2NjYyNA.Gw_25I.I1a5yuncW74ia__nLzZ0dh2513P9HpI0svc5Ps"
bot = commands.Bot(command_prefix = ".", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

@bot.command(description="Sends the bot's latency.") # this decorator makes a prefix command
async def send(ctx, user:discord.User, *, message):
    await user.send(f"Message from {ctx.author}: {message}")
    await ctx.send(f"Sent!")

@bot.user_command(name="Say thanks!")
async def thanks(ctx, member:discord.Member):
    await member.send(f"{ctx.author.name} says thanks!")
    await ctx.send("Thanks sent!")

@bot.message_command(name="Get raw data")
async def raw(ctx, message:discord.Message):
    await ctx.send(message)

@bot.command()
async def reload(ctx):
    for folder in os.listdir("Todo\Discord\Python Files\Cogs"):
        for file in os.listdir(f"Todo\Discord\Python Files\Cogs\{folder}"):
            if file.endswith(".py"):
                bot.reload_extension(name=f"Cogs.{folder}.{file[:-3]}")
                await ctx.send(f"{file} reloaded!")

for folder in os.listdir("Todo\Discord\Python Files\Cogs"):
        for file in os.listdir(f"Todo\Discord\Python Files\Cogs\{folder}"):
            if file.endswith(".py"):
                bot.load_extension(name=f"Cogs.{folder}.{file[:-3]}")
            

bot.run(TOKEN) # run the bot with the token

# read thru:
# cogs rules