# Copyright (C) 2021, A5taroth and iluvsoup
# This module has all information regarding the bot's commands.

import discord

from discord.ext import commands
from main import get_prefix

help_embed=discord.Embed(
    title="Help",
    description="Use `{0}help <cmd>` for more info".format(get_prefix)
)
help_embed.add_field(
    name=":rock: **General**",
    value=(
        ":ping_pong: Ping\n`{0}ping`\n\n"
        ":wave: Greet the new members\n`{0}welcome`\n\n"
        ":sunrise: Rise and shine\n`{0}goodmorning`\n\n"
        ":sleeping_accommodation: Don't look under your bed\n`{0}goodnight`\n\n"
    ).format(get_prefix)
)
help_embed.add_field(
    name=":game_die: **Fun**",
    value=(
        ":speaking_head: Get inspiring quotes\n`{0}quote`\n\n"
        ":8ball: Ask the Rock's ba- BIG BRAIN!\n`{0}rockball`\n\n"
    ).format(get_prefix)
)
help_embed.add_field(
    name=":tools: **Features in development**",
    value=(
        ":man_dancing: It's gif, NOT gif\n`{0}gif`\n\n"
        ":pancakes: The Pancake Emporium\n`{0}pancake`\n\n"
        ":red_car: F1.. Scuffed Edition\n`{0}race`\n\n"
        ":skull: Hangman. That's it.\n`{0}hangman`\n\n"
    ).format(get_prefix)
)
help_embed.add_field(
    name=":closed_lock_with_key: **Administrator**",
    value=(
        ":key: Prefix changer\n`{0}prefix`\n"
    ).format(get_prefix)
)
help_embed.set_footer(
    text="The Rock Bot v1.0 (c) 2021, A5taroth and iluvsoup"
)

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.group(
        name="help",
        invoke_without_command=True
    )
    async def help(self, ctx):
        help_embed.color=discord.Color.random()
        await ctx.send(embed=help_embed)

    @help.command(
        name="prefix"
    )
    async def prefix(self, ctx):
        prefix_embed=discord.Embed(
            title="Prefix",
            color=0x0ffad0,
            description=(
                "This command changes the command_prefix for the server.\n"
                "(Admins only.)"
            )
        )
        prefix_embed.add_field(
            name="Syntax",
            value="`{0}prefix <prefix>`".format(get_prefix)
        )
        await ctx.send(embed=prefix_embed)

    @help.command(
        name="me"
    )
    async def help_me(self, ctx):
        await ctx.send(
            (
                "{0.mention} If it's about your messed up "
                "life there's nothing I can do about it "
                "however if you need help regarding "
                "commands use `{1}help`"
            ).format(ctx.author, get_prefix)
        )

    @help.command(
        name="ping",
        aliases=["pong", "latency"]
    )
    async def ping(self, ctx):
        ping_embed=discord.Embed(
            title="Ping",
            color=0xFF4C30,
            description="The Rock will serve you some of those delicious :pancakes:"
        )
        ping_embed.add_field(
            name="Syntax",
            value="`{0}ping`".format(get_prefix)
        )
        await ctx.send(embed=ping_embed) 

    @help.command(
        name="pancake",
        aliases=["pc", "pancakes"]
    )
    async def pancake(self, ctx):
        pancake_embed=discord.Embed(
            title="Pancake",
            color=0xFFC219,
            description="The Rock will serve you some of those delicious :pancakes:"
        )
        pancake_embed.add_field(
            naem="Syntax",
            value="`{0}pancake`".format(get_prefix)
        )
        await ctx.send(embed=pancake_embed)

    @help.command(
        name="quote",
        aliases=["quotes", "q"]
    )
    async def quote(self, ctx):
        quote_embed=discord.Embed(
            title="Quote",
            color=0x1abc9c,
            description="The Rock will send a very inspiring quote that is guarenteed to be extremely knowledgeable."
        )
        quote_embed.add_field(
            name="Syntax",
            value="`{0}quote`".format(get_prefix)
        )
        await ctx.send(embed=quote_embed)

    @help.command(
        name="rockball",
        aliases=["rb", "8b", "8-ball", "8ball"]
    )
    async def rockball(self, ctx):
        rb_embed=discord.Embed(
            title="Ask the Rock's bal- BIG BRAIN :8ball:",
            color=0x000000,
            description="The Rock will try to answer your question with his infinite wisdom."
        )
        rb_embed.add_field(
            name="Syntax",
            value="`{0}rockball <question>`".format(get_prefix)
        )
        await ctx.send(embed=rb_embed)

    @help.command(
        name="w",
        aliases=["welcome"]
    )
    async def welcome(self, ctx):
        wembed=discord.Embed(
            title="Welcome",
            color=0xe67e22,
            description="The Rock will heartily welcome someone to the server."
        )
        wembed.add_field(
            name="Syntax",
            value="`{0}welcome <user>`".format(get_prefix)
        )
        await ctx.send(embed=wembed)

    @help.command(
        name="gm",
        aliases=["goodmorning"]
    )
    async def goodmorning(self, ctx):
        gm_embed=discord.Embed(
            title="Good Morning",
            color=0x3498db,
            description="The Rock will wish someone a good morning so they can feel accomplished in life."
        )
        gm_embed.add_field(
            name="Syntax",
            value="`{0}gm <user>".format(get_prefix)
        )
        await ctx.send(embed=gm_embed)

    @help.command(
        name="gn",
        aliases=["goodnight"]
    )
    async def goodnight(self, ctx):
        gn_embed=discord.Embed(
            title="Good Night",
            color=0x7289da,
            description="The Rock will wish you a good night so you can have sweet dreams ABOUT HIM."
        )
        gn_embed.add_field(
            name="Syntax",
            value="`{0}gn <user>".format(get_prefix)
        )
        await ctx.send(embed=gn_embed)

    @help.command(
        name="hangman",
        aliases=["hm"]
    )
    async def hangman(self, ctx):
        hangman_embed=discord.Embed(
            title="Hangman",
            color=0xff0100,
            description="It's hangman I dunno what you wanted but it's just hangman."
        )
        hangman_embed.add_field(
            name="Syntax",
            value="`{0}hangman`".format(get_prefix)
        )
        await ctx.send(embed=hangman_embed)

    @help.command(
        name="race",
        aliases=["r"]
    )
    async def race(self, ctx):
        race_embed=discord.Embed(
            title="Race",
            color=0xff0100,
            description="Race against another player in your vehicle of choice as the Rock cheers you on."
        )
        race_embed.add_field(
            name="Syntax",
            value="`{0}race`".format(get_prefix)
        )
        await ctx.send(embed=race_embed)

    @help.command(
        name="gif",
        aliases=["jif", "g"]
    )
    async def gif(self, ctx):
        gif_embed=discord.Embed(
            title="GIF",
            color=0xff0100,
            description="The Rock will post a gif matching the topic of your choice."
        )
        gif_embed.add_field(
            name="Syntax",
            value="`{0}gif`".format(get_prefix)
        )
        await ctx.send(embed=gif_embed)

        
def setup(bot):
    bot.add_cog(Help(bot))
    