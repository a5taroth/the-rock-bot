# Copyright (C) 2021, A5taroth and iluvsoup
# The main program where everything is put together.

import datetime, discord, os, random

from discord.ext import commands
from replit import db
from packages import webserver
from packages.config import GeneralConfig

GENERAL=GeneralConfig()

def get_prefix(bot, msg):
    if not msg.guild: return GENERAL.DEFAULT_PREFIX
    else : return db['prefix'][str(msg.guild.id)]


bot = commands.Bot(
    command_prefix=(get_prefix), 
    activity=discord.Activity(
        name="Face Off",
        type=discord.ActivityType.listening
    ),
    status = discord.Status.online
)
bot.remove_command("help")


@bot.event
async def on_ready():
    random.seed(datetime.time)
    print("{0.user} is now online.".format(bot))


@bot.event
async def on_guild_join(guild):
    db['prefix'][str(guild.id)]=GENERAL.DEFAULT_PREFIX


@bot.event
async def on_guild_remove(guild):
    del db['prefix'][str(guild.id)]


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


@bot.command(name="prefix")
@commands.guild_only()
@commands.has_permissions(administrator=True)
async def prefix(ctx, prefix):
    db['prefix'][str(ctx.guild.id)]=prefix
    await ctx.message.add_reaction('✅')

@prefix.error
async def prefix_error(self, ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.message.add_reaction('❌')

webserver.run()
bot.run(os.environ['TOKEN'])