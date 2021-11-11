# Copyright (C) 2021, A5taroth and iluvsoup
# This module will be home to the greatest panacke emporium backend ever.

import discord

from discord.ext import commands

class Pancake(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.group(
        name="pancake",
        aliases=["pc", "pancakes"],
        invoke_without_command=True
    )
    async def pancake(self, ctx):
        pancake_embed=discord.Embed(
            title=":tools: We're working on it!",
            color=0xffff00,
            description="This feature is in development."
        )

        await ctx.channel.send(
            embed=pancake_embed
        )


def setup(bot):
    bot.add_cog(Pancake(bot))
    