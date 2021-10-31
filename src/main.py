# The main program where everything runs (I mean it's called main.py)

import shit
import random
import discord
import datetime
import os
import webserver

@shit.bot.event
async def on_ready():
    random.seed(datetime.time)
    print(f"{shit.bot.user} is now online.")


@shit.bot.event
async def on_message(msg):
    await shit.bot.process_commands(msg)


@shit.bot.event
async def on_command_error(ctx, error):
    if isinstance(error, shit.commands.errors.MissingRequiredArgument):
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


webserver.keep_alive()
shit.bot.run(os.environ['TOKEN'])