# The headfile where everything is put together

import random
import discord
import datetime
import os

from packages import webserver
from discord.ext import commands
from config import PREFIX

bot = commands.Bot(
    command_prefix = PREFIX, 
    activity = discord.Activity(
        name="Face Off",
        details=f"Use {PREFIX}help to learn more.",
        type=discord.ActivityType.listening
    ),
    status = discord.Status.online
)
bot.remove_command("help")


@bot.event
async def on_ready():
    random.seed(datetime.time)
    print(f"{bot.user} is now online.")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send(
            embed=discord.Embed(
                title="Error69 occured",
                color=discord.Color.red(),
                description=(
'''
Arguments missing or syntax incorrect
Use $help <command> to learn the syntax
''' 
                )
            )
        )
    else: raise error

for file in os.listdir("./src/modules"):
    if file.endswith(".py"):
        bot.load_extension(f"modules.{file[0:-3]}")
        print(f"{file[0:-3]} is now loaded.")

webserver.keep_alive()

bot.run(os.environ['TOKEN'])