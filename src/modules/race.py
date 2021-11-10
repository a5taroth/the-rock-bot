import discord
from discord.ext import commands

class Race(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.group(
        name="race",
        aliases=["r"],
        invoke_without_command=True
    )
    async def race(self, ctx):
        await ctx.channel.send(
            embed = discord.Embed(
                title = ":tools: We're working on it!", 
                description = "This feautre is in development.",
                color = discord.Color.gold()
            )
        )

def setup(bot):
    bot.add_cog(Race(bot))