# Copyright (C) 2021, A5taroth and iluvsoup
# This module covers the quote functionality of the bot.

import discord, json

from discord.ext import commands
from urllib.request import urlopen
from packages.config import QuoteConfig

QUOTE_CONFIG=QuoteConfig()

class Quote(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.group(
        name="quote",
        aliases=["quotes", "q"],
        invoke_without_command=True
    )
    async def quote(self, ctx):
        QUOTE = json.load(urlopen(QUOTE_CONFIG.QUOTE_URL))[0]

        if QUOTE[2]=='': QUOTE[2]="Unknown"

        await ctx.channel.send(
            embed=discord.Embed(
                title="Very inspirational quote",
                color=discord.Color.random(),
                description=(
                    f"{QUOTE[1]}"
                    f"\n\n*- ~~{QUOTE[2]}~~ The Rock*"
                )
            )
        )


def setup(bot):
    bot.add_cog(Quote(bot))


'''
Quote Return Structure:
[
    [
        'QuoteID',
        'Quote',
        'Author'
    ]
]

'''
