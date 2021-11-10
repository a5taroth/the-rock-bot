import discord
import json

from discord.ext import commands
from urllib.request import urlopen
from packages.config import QUOTE_URL

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