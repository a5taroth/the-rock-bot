import discord, random

from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(
        name="welcome",
        aliases=["w"]
    )
    async def wellcum(self, ctx, *, arg:discord.Member):
        welcome_embed=discord.Embed(
            title=f"Welcome {arg.name}!"
        )
        welcome_embed.set_image(
            url=random.choice(
                [
                    "https://i.ibb.co/H4fPHq8/welcome-2.jpg",
                    "https://images-ext-2.discordapp.net/external/Vdc8YMnwFT0GHN1wvsZZgDcfnG2YiwXEAJ9kM3SZbr4/https/i.ibb.co/T8KD6Hp/welcome.jpg"
                ]
            )
        )

        await ctx.send(
            embed=welcome_embed
        )

    @commands.command(
        name="goodmorning",
        aliases=["gm"]
    )
    async def gudmorn(self, ctx):
        gm_embed=discord.Embed(
            title="Hope you have a wonderful day!"
        )
        gm_embed.set_image(
            url=random.choice(
                [
                    "https://i.ibb.co/TWbFHtL/gm3.jpg",
                    "https://i.ibb.co/44xhwC9/gm2.jpg"
                ]
            )
        )

        await ctx.send(
            embed=gm_embed
        )


    @commands.command(
        name="goodnight",
        aliases=["gn"]
    )
    async def gudnite(self, ctx):
        gn_embed=discord.Embed(
            title="Have a great night!"
        )
        gn_embed.set_image(
            url=random.choice(
                [
                    "https://i.ibb.co/kgw9Fk0/gn1.jpg",
                    "https://i.ibb.co/0czbz1V/gn2.jpg"
                ]
            )
        )

        await ctx.send(
            embed=gn_embed
        )


def setup(bot):
    bot.add_cog(Greetings(bot))
