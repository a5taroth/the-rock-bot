# okay so this is basically the rocks heart if you break it
# he will die so dont break it but it also tells him what
# to do and how to do so plz dont break it

#TODO: Pancake command, quote command, image command, music possibly?

import requests # do we really need this i mean we are using urlopen

from random import choice # for choosing :)
from urllib.request import urlopen # for opening the url
from json import load # for the json
from discord import Color, Embed, Game, File # self explanatory
from os import environ # for the token
from discord.ext import commands # dunno what this does but we need it for the bot to work lmao
from webserver import keep_alive # function to keep the webserver running

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

possible_image_paths = ["chains.jpg", "hercules.jpg", "idk.jpg", "muscles.webp", "pancakes.webp"]

url = "http://www.famous-quotes.uk/api.php?id=random&minpop=75"
json = load(urlopen(url))

quote = {
    "desc": "This is the description.",
    "auth": "default",
    # "json": ""
}

# Column 1: Quote id in our database
# Column 2: Quote
# Column 3: Author


@bot.event
async def on_ready():
    print("Executing on {.user}".format(bot))
    # print(load(quote["json"]))

    await bot.change_presence(
        activity=Game(
            name="it's about drive, it's about power"
        )
    )


    @bot.command(
        name="help",
        help="THIS IS HELP YOU IDIOT",
        aliases=[]
    )
    async def help(ctx):
        await ctx.channel.send("This is help.")


    @bot.command(
        name="ping",
        help="The Rock will tell you how fast his latency is in milliseconds!",
        pass_context=True,
        aliases=["pingpong", "pong", "latency"]
    )
    async def ping(ctx):
        await ctx.send(":ping_pong: Pong! **{round(.latency*1000)} ms**".format(bot))


    @bot.command(
        name="pancake",
        aliases=["pc", "pancakes"]
    )
    async def make_pancakes(ctx):
        ctx.channel.send(
            embed=Embed(
                title="Making Pancakes",
                description="The Rock is making pancakes."
            )
        )


    @bot.command(
        name="quote",
        help="The Rock will send a very inspiring quote that is guarenteed to be extremely knowledgeable.",
        aliases=[]
    )
    async def send_a_quote(ctx):
        global json

        json=load(urlopen(url))

        await ctx.channel.send(
            embed=Embed(
                title="Quote",
                description=(
                    "{}"
                    " -The Rock ({})".format(quote["desc"], quote["auth"])
                )
            )
        )


    @bot.command(
        name="image",
        help="The Rock will flex his muscles... or not.",
        aliases=[]
    )
    async def send_those_muscles(ctx):
        await ctx.channel.send(
            embed=Embed(
                title="Massive Muscles",
                color = Color.blue(),
                description="The image is... ~~not yet~~ now available."
            ),
            file=File(
                f"the_rock_images/{choice(possible_image_paths)}"  
            )
        )

keep_alive() # cpr
TOKEN = environ['TOKEN']
bot.run(TOKEN)
print(json)
