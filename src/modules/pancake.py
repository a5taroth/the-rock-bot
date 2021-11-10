import discord
import time

from discord.ext import commands
from replit import db

bussiness_running=False


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    
    return False


class Pancake(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.group(
        name="pancake",
        aliases=["pc", "pancakes"],
        invoke_without_command=True
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
        aliases=["reg"]
    )
    async def reg(self, ctx):
        if ctx.author in db:
            await ctx.send(
                embed=discord.Embed(
                    title="Uh oh",
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
        aliases=["bal"]
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

    @pancake.command(
        name="run"
    )
    async def run(self, ctx):
        global bussiness_running

        if not bussiness_running:
            bussiness_running=True
            bussiness_running=countdown(30)
        else: 
            await ctx.send(
                embed=discord.Embed(
                    title="Error84 occurred",
                    color=0xff0000,
                    description="Your shop is already running."
                )
            )


def setup(bot):
    bot.add_cog(Pancake(bot))