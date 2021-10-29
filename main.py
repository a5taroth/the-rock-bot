# The main program where everything runs (I mean it's called main.py)

import discord
import random
import json
import images
import response

from datetime import time
from urllib.request import urlopen
from os import environ 
from discord.ext import commands 
from webserver import keep_alive 

PREFIX = "$"

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

players = []
CHOICE_TYPE=["n", "p", "c"] # for rockball

possible_words = ("rock", "muscle", "exercise", "pancakes")
hangman_word = random.choice(possible_words) 

quote_url = "http://www.famous-quotes.uk/api.php?id=random&minpop=75"

help_embed=discord.Embed(
    title="Help",
    description=f"Use {PREFIX}help <command> for more info",
)
help_embed.add_field(
    name="Features",
    value=(
'''
-> The Rock Ball (entirely different from the Rock's balls)
-> Quote
-> Ping
'''
    )
)
help_embed.add_field(
    name="Games",
    value=(
'''
-> Pancake Empire
-> Hangman
-> Car Racing
'''
    )
)

@bot.event
async def on_ready():
    random.seed(time)
    print(f"{bot.user} is now online.")


@bot.group(
    name="help",
    invoke_without_command=True
)
async def help(ctx):
    await ctx.send(embed=help_embed)

@help.command()
async def ping(ctx):
    await ctx.send(
        embed=discord.Embed(
            title="Ping",
            description="Tells you how fast The Rock can eat 100 pancakes."
        )
    )


@help.command()
async def pancake(ctx):
    await ctx.send(
        embed=discord.Embed(
            title="Pancake",
            description="The Rock will serve you some of those delicious :pancakes:"
        )
    )

@help.command(
    name="hangman",
    aliases=["hg", "manhang?"]
)
async def hangman_help(ctx):
    await ctx.send(
        embed=discord.Embed(
            title="Hangman",
            description="Race against another player in your vehicle of choice as the Rock cheers you on."
        )
    )


@bot.command(
    name="ping",
    pass_context=True,
    aliases=["pingpong", "pong", "latency"]
)
async def _ping(ctx):
  await ctx.send(f":ping_pong: Pong! **{round(bot.latency*1000)} ms**")


@bot.command(
    name="pancake",
    aliases=["pc", "pancakes"]
)
async def _pancake(ctx):
    _embed=discord.Embed(
        title="Error 69",
        description="This feature is in development."  )
  
    await ctx.channel.send(
        embed=_embed
    )
  
@bot.command(
    name="quote",
    help="The Rock will send a very inspiring quote that is guarenteed to be extremely knowledgeable.",
    aliases=["quotes", "q", "i_am_depressed", "nobody_will_ever_find_out_that_this_is_an_alias"]
)
async def quote(ctx):
    quote = json.load(urlopen(quote_url))[0] 
    # The [0] is because the api returns a nested array
    # -> quote[0] = ID 
    # -> quote[1] = Quote
    # -> quote[2] = Author

    await ctx.channel.send(
        embed=discord.Embed(
            title="Very inspirational quote",
            description=(
                f"{quote[1]}"
                f"\n*- ~~{quote[2]}~~ The Rock*"
            ),
            color = discord.Color.teal()
        )
    )

@bot.command(
    name="image",
    help="But first, let me take a selfie!",
    aliases=["img","photo"]
)
async def image(ctx):
    await ctx.channel.send(
        file=discord.File(
            f"images/{random.choice(images.image_paths)}"
        )
    )


@bot.group(
    name="race",
    aliases=["vroom", "vroom-vroom"],
    invoke_without_command=True
)
async def race(ctx, arg:str):
    await ctx.channel.send(
        embed = discord.Embed(
            title = "Bumpy Ride by ~~Mohambi~~ The Rock", 
            description = "Atleast two players needed to begin.",
            color = discord.Color.red()
        )
    )


@race.command(
    name="start",
    aliases=["begin", "s"]
)
async def race_start(ctx):
    await ctx.send("Starting the race.")


@bot.command(
    name="hangman",
    aliases=["hm", "manhang?"]
)
async def hang_the_man(ctx):
    await ctx.send(
        embed=discord.Embed(
            title="Hangman",
            description="This feature is in development."
        )
    )


@bot.command(
    name="rockball",
    aliases=["ask-8ball", "magic-8ball", "8b", "8-ball", "8ball", "rb"]
)
async def rock_hard_balls(ctx):
    choice_embed=discord.Embed(
        title=":8ball: The Almighty Rock Ball"
    )
    
    NPC_CHOICE=random.choice(CHOICE_TYPE)
    if NPC_CHOICE=='n':
        response.choice=random.choice(response.neg)
        choice_embed.color=discord.Color.red()
    elif NPC_CHOICE=='p':
        response.choice=random.choice(response.pos)
        choice_embed.color=discord.Color.green()
    else:
        response.choice=random.choice(response.non_com)
        choice_embed.color=discord.Color.gold()

    choice_embed.description=response.choice
    choice_embed.set_thumbnail(url="https://discord.com/assets/0cfd4882c0646d504900c90166d80cf8.svg")

    
    await ctx.send(
        embed=choice_embed
    )


keep_alive() 
bot.run(environ['TOKEN'])

'''
Discord- Scuffed Edition
>

'''