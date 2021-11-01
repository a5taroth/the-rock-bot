import discord
import json
import os

from discord.ext import commands
from urllib.request import urlopen
from config import QUOTE_URL

class Quote(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.group(
        name="quote",
        aliases=["quotes", "q"],
        invoke_without_command=True
    )
    async def quote(self, ctx):
        QUOTE = json.load(urlopen(QUOTE_URL))[0]

        # QUOTE[0] = ID 
        # QUOTE[1] = Quote
        # QUOTE[2] = Author

        if QUOTE[2]=='': QUOTE[2]="Unknown"
#why are you on your school computer at this time of the day (i mean night)

        await ctx.channel.send(
            embed=discord.Embed(
                title="Very inspirational quote",
                color=0x1abc9c,
                description=(
                    f"{QUOTE[1]}"
                    f"\n\n*- ~~{QUOTE[2]}~~ The Rock*"
                )
            )
        )

def setup(bot):
    bot.add_cog(Quote(bot))