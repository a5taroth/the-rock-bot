import discord
from discord.ext import commands
from replit import db

class Pancake(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.group(
        name="pancake",
        aliases=["pc", "pancakes"],
        invoke_without_command=True # what does this do -> for extra commands
    )
    async def pancake(self, ctx):
        embed=discord.Embed(
            title=":tools: We're working on it!",
            color=0xffff00,
            description="This feature is in development."
        )

        await ctx.channel.send(
            embed=embed
        )

    @pancake.command(
        name="register",
        aliases=["r", "reg"]
    )
    async def reg(self, ctx):
        if ctx.author in db:
            await ctx.send(
                embed=discord.Embed(
                    title="Error196 occured",
                    color=0xff0000,
                    description="User already registered. Use `$help pancake` to learn more."
                )
            )
        db[ctx.author]={
            "balance":0,
            "pancakes":0,
            "floors":0,
            "furn_level":0,
            "advertizing":False
        }
        await ctx.send(
            embed=discord.Embed(
                title="Account registered successfully",
                color=0xffff00,
                description="Use `$pancake balance` to learn more about your current financial status."
            )
        )

    @pancake.command(
        name="balance",
        aliases=["b", "bal"]
    )
    async def bal(self, ctx):
        pancake_bal=discord.Embed(
            title=f"{ctx.author.display_name}'s statistics",
            color=0xffff00
        )
        pancake_bal.add_field(
            name="Balance",
            value=db[ctx.author]["balance"]
        )
        pancake_bal.add_field(
            name="Pancakes sold",
            value=db[ctx.author]["pancakes"]
        )

        await ctx.send(
            embed=pancake_bal
        )

def setup(bot):
    bot.add_cog(Pancake(bot))