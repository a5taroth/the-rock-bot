# The main program where everything is put together.

import datetime, discord, os, random

from discord.ext import commands
from packages import webserver
from packages.config import GeneralConfig

GENERAL=GeneralConfig()

bot = commands.Bot(
    command_prefix = GENERAL.PREFIX, 
    activity = discord.Activity(
        name="Face Off",
        details=f"Use {GENERAL.PREFIX}help to learn more.",
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
                title="An error occured :(",
                color=0xca0000,
                description=(
                    "Use `$help <cmd>` to learn the syntax\n"
                    "`missing required argument or incorrect syntax`"
                )
            )
        )
    elif isinstance(error, commands.errors.MemberNotFound):
        await ctx.send(
            embed=discord.Embed(
                title="An error occured :(",
                color=0xca0000,
                description=(
                    "Are you sure the person is a member of this server?"
                )
            )
        )
    
    else: raise error


@bot.event
async def on_message(ctx):
    ctx.content=ctx.content.lower()
    
    await bot.process_commands(ctx)


for file in os.listdir("./src/modules"):
    if file.endswith(".py"):
        bot.load_extension(f"modules.{file[0:-3]}")
        print(f"{file[0:-3]} is now loaded.")

webserver.run()

bot.run(os.environ['TOKEN'])