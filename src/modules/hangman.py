import discord

from discord.ext import commands

class Hangman(commands.Cog):
    def __init__(self, bot: commands.Cog):
        self.bot=bot
    
    @commands.command(
        name="hangman",
        aliases=["hm"]
    )
    async def hangman(self, ctx):
        await ctx.send(
            embed=discord.Embed(
                title=":tools: We're working on it!",
                description="This feature is in development.",
                color=0xffff00
            )
        )

def setup(bot):
    bot.add_cog(Hangman(bot))