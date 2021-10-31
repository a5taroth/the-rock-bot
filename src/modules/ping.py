from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.group(
        name="ping",
        aliases=["pingpong", "pong", "latency"],
        invoke_without_command=True
    )
    async def _ping(self, ctx):
        await ctx.send(f":ping_pong: Pong! **{round(self.bot.latency*1000)} ms**")

def setup(bot):
    bot.add_cog(Ping(bot))