import discord
from discord.ext import commands

class Gif(commands.Cog):
    def __init__(self, bot: commands.Cog):
        self.bot=bot
    
    @commands.command(
        name="gif",
        aliases=["g","jif"]
    )
    async def gif(self, ctx):
        await ctx.send(
            embed=discord.Embed(
                title=":tools: We're working on it!",
                description="This feature is in development.",
                color=discord.Color.gold()
            )
        )

def setup(bot):
    bot.add_cog(Gif(bot))