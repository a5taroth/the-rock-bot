# This is the back-end of the backend where all the shit works
# That's why it's called shit

import discord
import random
import json
import images
import response

from urllib.request import urlopen
from discord.ext import commands 

PREFIX="$"
DOUBLE_LINE_BREAK="\n\n"

players = []
CHOICE_TYPE=["n", "p", "c"] # for rockball

possible_words = ("rock", "muscle", "exercise", "pancakes")
hangman_word = random.choice(possible_words) 

quote_url = "http://www.famous-quotes.uk/api.php?id=random&minpop=75"

# SETUP
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


help_embed=discord.Embed(
    title="Help",
    description=f"Use {PREFIX}help <command> for more info",
)
help_embed.add_field(
    name=":rock: FEATURES",
    value=(
'''
:speaking_head: Inspiring quotes
    `$quote`\n
:ping_pong: Ping (Yes, that's it)
    `$ping`\n
:man_dancing: Stop arguing: it's gif (not gif)
    `$gif`\n
:wave: Greet your friends (friends are optional)
    `$welcome`\n
:sunrise: WAKE UP WAKE UP WAKE UP
    `$goodmorning`\n
:sleeping_accommodation: Don't look under your bed
    `$goodnight`\n
'''
    )
)
help_embed.add_field(
    name=":game_die: FUN",
    value=(
'''
:8ball: Ask the Rock's ball
    `$8ball`\n
:thinking_face: Fun facts about The Rock
    `$trivia`\n
:pancakes: The Pancake Empire
    `$pancake`\n
:skull: Hangman but bad
    `$hangman`\n
:red_car: F1: Scuffed Edition
    `$race`\n
'''
    )
)
help_embed.set_footer(
  text=(
    '''
Some features are still in development 🛠️

The Rock Bot v1.0 ©️
    '''
    )
)

@bot.group(
    name="help",
    invoke_without_command=True
)
async def help(ctx):
    await ctx.author.send(embed=help_embed)

# Ping:
@bot.command(
    name="ping",
    pass_context=True,
    aliases=["pingpong", "pong", "latency"]
)
async def _ping(ctx):
  await ctx.send(f":ping_pong: Pong! **{round(bot.latency*1000)} ms**")

@help.command()
async def ping(ctx):
    await ctx.send(
        embed=discord.Embed(
            title="Ping",
            description="Tells you how fast The Rock can eat 100 pancakes."
        )
    )

# Pancake
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

@help.command(
    name="pancake",
    aliases=["pc", "pancakes"]
)
async def pancake(ctx):
    await ctx.send(
        embed=discord.Embed(
            title="Pancake",
            description="The Rock will serve you some of those delicious :pancakes:"
        )
    )


@bot.command(
    name="quote",
    aliases=["quotes", "q"]
)
async def quote(ctx):
    QUOTE = json.load(urlopen(quote_url))[0] 

    # The [0] is because the api returns a nested array
    # QUOTE[0] = ID 
    # QUOTE[1] = Quote
    # QUOTE[2] = Author

    if QUOTE[2]=='': QUOTE[2]="Unknown"

    await ctx.channel.send(
        embed=discord.Embed(
            title="Very inspirational quote",
            description=(
                f"{QUOTE[1]}"
                f"{DOUBLE_LINE_BREAK}*- ~~{QUOTE[2]}~~ The Rock*"
            ),
            color = discord.Color.teal()
        )
    )

@help.command(
    name="quote",
    aliases=["quotes", "q"]
)
async def cool_quote(ctx):
    await ctx.send(
        embed=discord.Embed(
            title="Quote",
            description="The Rock will send a very inspiring quote that is guarenteed to be extremely knowledgeable."
        )
    )


@bot.command(
    name="rockball",
    aliases=["ask-8ball", "magic-8ball", "8b", "8-ball", "8ball", "rb"]
)
async def rock_hard_balls(ctx, *, arg:str):
    choice_embed=discord.Embed(
        title="The Almighty Rock Ball     :8ball:"
    )
    
    NPC_CHOICE=random.choice(CHOICE_TYPE)
    if NPC_CHOICE=='n':
        response.choice=random.choice(response.neg)
        choice_embed.color=discord.Color.red()
    elif NPC_CHOICE=='p':
        response.choice=random.choice(response.pos)
        choice_embed.color=discord.Color.green()
    elif NPC_CHOICE=='c':
        response.choice=random.choice(response.non_com)
        choice_embed.color=discord.Color.gold()

    choice_embed.description=response.choice
    choice_embed.set_thumbnail(url="https://discord.com/assets/0cfd4882c0646d504900c90166d80cf8.svg")

    
    await ctx.send(
        embed=choice_embed
    )

@help.command(
    name="rockball",
    aliases=["ask-8ball", "magic-8ball", "8b", "8-ball", "8ball", "rb"]
)
async def those_8_balls_tho(ctx):
    await ctx.send(
        embed=discord.Embed(
            title="Quote",
            description="The Rock will try to answer your question with his infinite wisdom."
        )
    )


@bot.command(
    name="welcome",
    aliases=["w"]
)
async def wellcum(ctx, *, arg:discord.Member):
    welcome_embed=discord.Embed(
        title=f"Welcome {arg.name}!"
    )
    welcome_embed.set_image(
        url=random.choice(
            [
                "https://i.ibb.co/H4fPHq8/welcome-2.jpg",
                "https://images-ext-2.discordapp.net/external/Vdc8YMnwFT0GHN1wvsZZgDcfnG2YiwXEAJ9kM3SZbr4/https/i.ibb.co/T8KD6Hp/welcome.jpg"
            ]
        )
    )

    await ctx.send(
        embed=welcome_embed
    )

@help.command(
    name="w",
    aliases=["welcome"]
)
async def gudmorn_help(ctx):
    await ctx.send(
        embed=discord.Embed(
            title="Welcome",
            description="The Rock will heartily welcome you  to the server."
        )
    )


@bot.command(
    name="goodmorning",
    aliases=["gm"]
)
async def gudmorn(ctx):
    gm_embed=discord.Embed(
        title="Hope you have a wonderful day!"
    )
    gm_embed.set_image(
        url=random.choice(
            [
                "https://i.ibb.co/TWbFHtL/gm3.jpg",
                "https://i.ibb.co/44xhwC9/gm2.jpg"
            ]
        )
    )

    await ctx.send(
        embed=gm_embed
    )

@help.command(
    name="gm",
    aliases=["goodmorning"]
)
async def gudmorn_help(ctx):
    await ctx.send(
        embed=discord.Embed(
            title="Good Morning",
            description="The Rock will wish you a good morning so you can feel accomplished in life."
        )
    )


@bot.command(
    name="goodnight",
    aliases=["gn"]
)
async def gudnite(ctx):
    gn_embed=discord.Embed(
        title="Have a great night!"
    )
    gn_embed.set_image(
        url=random.choice(
            [
                "https://i.ibb.co/kgw9Fk0/gn1.jpg",
                "https://i.ibb.co/0czbz1V/gn2.jpg"
            ]
        )
    )

    await ctx.send(
        embed=gn_embed
    )

@help.command(
    name="gn",
    aliases=["goodnight"]
)
async def gudnite_help(ctx):
    await ctx.send(
        embed=discord.Embed(
            title="Good Night",
            description="The Rock will wish you a night so you can have sweet dreams."
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


