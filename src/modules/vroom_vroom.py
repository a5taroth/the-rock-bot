import discord

from discord.ext import commands 

in_progress=False

class Race(commands.Cog): # I swear I am not racist    
    def __init__(self, bot: commands.Bot):
        self.bot=bot

    @commands.group(
        name="race",
        aliases=["vroom", "vroom-vroom"],
        invoke_without_command=True
    )
    async def race(self, ctx, arg:str):
        await ctx.channel.send(
            embed = discord.Embed(
                title = ":tools: We're working on it!", 
                description = "This feautre is in development.",
                color = 0xffff00
            )
        )


    @race.command(
        name="start",
        aliases=["begin", "s"]
    )
    async def race_start(self, ctx):
        await ctx.send("Starting the race.")


def setup(bot: commands.Bot):
    bot.add_cog(Race(bot))