# okay so this is basically the rocks heart if you break it
# he will die so dont break it but it also tells him what
# to do and how to do so plz dont break it

#TODO: Pancake command, quote command, image command, music possibly?

import requests
import json
import random

from discord import Embed, Game
from os import environ
from discord.ext import commands
from webserver import keep_alive

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")


@bot.event
async def on_ready():
    print("Executing on {0.user}".format(bot))

    await bot.change_presence(activity=Game(
        name="it's about drive, it's about power"))

    @bot.command(name="ping",
                 pass_context=True,
                 aliases=["pingpong", "pong", "latency"])
    async def ping(ctx):
        await ctx.send(f":ping_pong: Pong! **{round(bot.latency*1000)} ms**")


@bot.command(
    name="quote",
    help=
    "The Rock will send a very inspiring quote that is guarenteed to be xtremely knowledgeable.",
    aliases=[]
)
async def send_a_quote(_msg):
    _msg.channel.send(
        embed=Embed(title="Quote", desc="Finding good quotes is hard okay?"))


# @bot.event
# async def on_message(msg):
#     if msg.content.strip().lower() == ""

keep_alive()
TOKEN = environ['TOKEN']
bot.run(TOKEN)
