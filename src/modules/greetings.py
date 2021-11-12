# Copyright (C) 2021, A5taroth and iluvsoup
# This module covers the greeting mechanism of the bot.

import discord, random

from discord.ext import commands

class Phrases():
    GOOD_MORNING_NULL=[
        "What a great to day to workout.",
        "Good morning!",
        "Rise and shine!",
        "The Rock is pleased to see you."
    ]

    GOOD_MORNING_REG=[
        "The Rock wishes you a good morning, {}.",
        "Good morning, {}!",
        "Rise and shine, {}!"
    ]

    GOOD_NIGHT_NULL=[
        "Sleep tight and have some wet dreams of your waifus!", 
        "Good night!",
        "Have a great night!",
        "Don't let the bed bugs bite!"
    ]

    GOOD_NIGHT_REG=[
        "1 out of 8 people die in their sleep.\nSleep tight, {}!", 
        "Good night, {}!",
        "Have a great night, {}!",
        "Don't let the bed bugs bite, {}!"
    ]

    WELCOME=[
        "The rock welcomes you, {}!",
        "Hello {}!",
        "Welcome, {}!",
        "Greetings from The Rock, {}!"
    ]


class Images():
    WELCOME=[
        "https://i.ibb.co/H4fPHq8/welcome-2.jpg",
        "https://IMAGES-ext-2.discordapp.net/external/Vdc8YMnwFT0GHN1wvsZZgDcfnG2YiwXEAJ9kM3SZbr4/https/i.ibb.co/T8KD6Hp/welcome.jpg",
        "https://i.ibb.co/4W5gMVb/welcum.jpg",
        "https://i.ibb.co/KjVy0Lg/welcum-rock.jpg",
        "https://i.ibb.co/mhvspPB/cyan-cum.jpg"
    ]

    GOODMORNING=[
        "https://i.ibb.co/TWbFHtL/gm3.jpg",
        "https://i.ibb.co/44xhwC9/gm2.jpg",
        "https://i.ibb.co/JQdzRt9/hard-work.jpg"
    ]

    GOODNIGHT=[
        "https://i.ibb.co/kgw9Fk0/gn1.jpg",
        "https://i.ibb.co/0czbz1V/gn2.jpg",
        "https://i.ibb.co/r7Q7LtS/chains-gn.jpg"
    ]


CHOICE=Phrases()
IMAGES=Images()

class Greeting(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(
        name="welcome",
        aliases=["w"]
    )
    @commands.guild_only()
    async def welcome(self, ctx, *, arg:discord.Member):
        TITLE=random.choice(CHOICE.WELCOME)
        
        welcome_embed=discord.Embed(
            title=TITLE.format(arg.name)
        )
        welcome_embed.set_image(
            url=random.choice(IMAGES.WELCOME)
        )

        await ctx.send(
            embed=welcome_embed
        )

    @commands.command(
        name="goodmorning",
        aliases=["gm"]
    )
    @commands.guild_only()
    async def goodmorning(self, ctx, *, arg:discord.Member=''):
        if arg!='':
            TITLE=random.choice(CHOICE.GOOD_MORNING_REG)
            gm_embed=discord.Embed(
                title=TITLE.format(arg.name)
            )
        else:
            TITLE=random.choice(CHOICE.GOOD_MORNING_NULL)
            gm_embed=discord.Embed(
                title=TITLE
            ) 

        gm_embed.set_image(
            url=random.choice(
                IMAGES.GOODMORNING
            )
        )

        await ctx.send(
            embed=gm_embed
        )


    @commands.command(
        name="goodnight",
        aliases=["gn"]
    )
    @commands.guild_only()
    async def goodnight(self, ctx, *, arg: discord.Member="Null"): 
        if arg=="Null":
            TITLE=random.choice(CHOICE.GOOD_NIGHT_NULL)
        else:
            TITLE=random.choice(CHOICE.GOOD_NIGHT_REG)
       
        if arg=="Null":
            gn_embed=discord.Embed(
                title=TITLE
            )
        else:
            gn_embed=discord.Embed(
                title=TITLE.format(arg.name)
            )   
        gn_embed.set_image(
            url=random.choice(
                IMAGES.GOODNIGHT
            )
        )

        await ctx.send(embed=gn_embed)


def setup(bot):
    bot.add_cog(Greeting(bot))
