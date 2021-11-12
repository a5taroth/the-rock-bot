# Copyright (C) 2021, A5taroth and iluvsoup
# This module contains all infrastructure (responses) for the rockball.

import discord, random

from discord.ext import commands

class Responses():
    AFFIRMATIVE=[
        "THE ROCK CERTIFIES.",
        "CONFIRMED.",
        "OBVIOUSLY.",
        "IT IS THE TRUTH.",
        "THE ROCK SAYS SO.",
        "THE ROCK APPROVES.",
        "CORRECT.",
        "SEEMS SO.",
        "I BELIEVE SO.",
        "TRUST ME."
    ]

    NEGATIVE=[
        "NOT CERTIFIED.",
        "DON'T THINK SO.",
        "THE ROCK SAYS NO.",
        "FALSE.",
        "DON'T TRUST EVERYTHING YOU HEAR."
    ]

    NEUTRAL=[
        "I AM AFRAID I DO NOT KNOW.",
        "I CANNOT TELL RIGHT NOW>",
        "CAN YOU REPEAT THAT?",
        "I'M HAVING A BIT OF TROUBLE ANSWERING.",
        "SHOO! NOT NOW I'M CONCENTRATING.",
        "NOW IS NOT THE TIME TO ANSWER THAT>",
        "DO YOU HAVE NO BRAINS!? IT'S OBVIOUS."
    ]

RESPONSES=Responses()

class RockBall(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.group(
        name="rockball",
        aliases=["rb", "8b", "8-ball", "8ball"],
        invoke_without_command=True
    )
    async def rock_hard_balls(self, ctx, *, arg:str):
        choice_embed=discord.Embed(
            title="The Almighty Rock Ball :8ball:"
        )

        RESPONSE_TYPE=random.choice(
            [
                RESPONSES.AFFIRMATIVE,
                RESPONSES.NEGATIVE,
                RESPONSES.NEUTRAL                
            ]
        )

        RESPONSE=random.choice(
            RESPONSE_TYPE
        )
        
        if RESPONSE_TYPE==RESPONSES.AFFIRMATIVE: choice_embed.color=discord.Color.green()
        elif RESPONSE_TYPE==RESPONSES.NEGATIVE: choice_embed.color=discord.Color.red()
        else: choice_embed.color=discord.Color.gold() 

        choice_embed.description=RESPONSE

        await ctx.send(embed=choice_embed)

def setup(bot):
    bot.add_cog(RockBall(bot))
    