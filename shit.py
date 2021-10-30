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

bot = commands.Bot(
  command_prefix = PREFIX, 
  activity = discord.Activity(
    name="Face Off",
    details="Use {}help to learn more.".format(PREFIX),
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

@bot.group(
    name="help",
    invoke_without_command=True
)
async def help(ctx):
    await ctx.send(embed=help_embed)

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
    # -> QUOTE[0] = ID 
    # -> QUOTE[1] = Quote
    # -> QUOTE[2] = Author

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
    welcome_embed.set_image(url="https://images-ext-2.discordapp.net/external/2Mnjz4YHheUtHGgVb-BOzddY7DA2lCVcOBBsoC-NV7o/https/cdn-longterm.mee6.xyz/plugins/commands/images/759279990277144657/1c2ceb1c3e4ab52c94b5ae1e688a25816ccc848f6f79ea5af0f5d83948d2dd98.png?width=734&height=413")

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
    gm_embed.set_image(url="https://images-ext-2.discordapp.net/external/0y_MxifvmjxtlzOaD0kq_aKV1KDTY8Bwdht4zaPNmWQ/https/media.discordapp.net/attachments/842242244312432700/842900017630674974/unknown.png?width=738&height=413")

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
    gn_embed.set_image(url="https://images-ext-2.discordapp.net/external/0y_MxifvmjxtlzOaD0kq_aKV1KDTY8Bwdht4zaPNmWQ/https/media.discordapp.net/attachments/842242244312432700/842900017630674974/unknown.png?width=738&height=413")

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


