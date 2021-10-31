import discord

from config import PREFIX
from discord.ext import commands


help_embed=discord.Embed(
    title="Help",
    color=0xffffff,
    description=f"Use {PREFIX}help <command> for more info",
)
help_embed.add_field(
    name=":rock: FEATURES",
    value=(
'''
:speaking_head: Inspiring quotes
    `$quote`\n
:ping_pong: Ping (Bonk)
    `$ping`\n
:man_dancing: It's gif NOT gif
    `$gif`\n
:wave: Greet the new members, you jerk
    `$welcome`\n
:sunrise: WAKE UP WAKE UP WAKE UP
    `$goodmorning`\n
:sleeping_accommodation: There's no demon under your bed
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
The Rock Bot v1.0 (c) 2021, A5taroth and iluvsoup
'''
    )
)

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.group(
        name="help",
        invoke_without_command=True
    )
    async def help(self, ctx):
        await ctx.send(embed=help_embed)

    @help.command(
        name="pancake",
        aliases=["pc", "pancakes"]
    )
    async def pancake(self, ctx):
        await ctx.send(
            embed=discord.Embed(
                title="Pancake",
                color=0xffff00,
                description="The Rock will serve you some of those delicious :pancakes:"
            )
        )

    @help.command(
        name="quote",
        aliases=["quotes", "q"]
    )
    async def cool_quote(self, ctx):
        await ctx.send(
            embed=discord.Embed(
                title="Quote",
                color=0x1abc9c,
                description="The Rock will send a very inspiring quote that is guarenteed to be extremely knowledgeable."
            )
        )

    @help.command(
        name="rockball",
        aliases=["ask-8ball", "magic-8ball", "8b", "8-ball", "8ball", "rb"]
    )
    async def those_8_balls_tho(self, ctx):
        await ctx.send(
            embed=discord.Embed(
                title="Ask the Rock's ball :8ball:",
                color=0x000000,
                description="The Rock will try to answer your question with his infinite wisdom."
            )
        )

    @help.command(
        name="w",
        aliases=["welcome"]
    )
    async def welcome_help(self, ctx):
        await ctx.send(
            embed=discord.Embed(
                title="Welcome",
                color=0xe67e22,
                description="The Rock will heartily welcome you  to the server."
            )
        )

    @help.command(
        name="gm",
        aliases=["goodmorning"]
    )
    async def gudmorn_help(self, ctx):
        await ctx.send(
            embed=discord.Embed(
                title="Good Morning",
                color=0x3498db,
                description="The Rock will wish you a good morning so you can feel accomplished in life."
            )
        )

    @help.command(
        name="gn",
        aliases=["goodnight"]
    )
    async def gudnite_help(self, ctx):
        await ctx.send(
            embed=discord.Embed(
                title="Good Night",
                color=0x7289da,
                description="The Rock will wish you a night so you can have sweet dreams."
            )
        )

    @help.command(
        name="hangman",
        aliases=["hg", "manhang?"]
    )
    async def hangman_help(self, ctx):
        await ctx.send(
            embed=discord.Embed(
                title="Hangman",
                color=0xff0100,
                description="Race against another player in your vehicle of choice as the Rock cheers you on."
            )
        )


def setup(bot):
    bot.add_cog(Help(bot))