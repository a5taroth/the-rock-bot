# Copyright (C) 2021, A5taroth and iluvsoup
# This module sends the current latency when requested.

import discord

from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(
        name="ping",
        aliases=["pingpong", "pong", "latency"],
    )
    async def ping(self, ctx):
        await ctx.send(
            embed=discord.Embed(
                title="Latency",
                description=":ping_pong: Pong! **{0} ms**".format(round(self.bot.latency*1000))
            )
        )

def setup(bot):
    bot.add_cog(Ping(bot))
    