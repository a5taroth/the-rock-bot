# i might've broken this
# couldnt test it out so i have no clue
# im not used to python syntax lmao

import discord
import random

from discord.ext import commands
from packages import rockball

CHOICE_TYPES=[rockball.pos,rockball.neg,rockball.non_com]
EMBED_COLORS=[discord.Color.green(),discord.Color.red(),discord.Color.gold()]

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
      
      CHOICE=random.randrange(1,3)
      
      CHOICE_TYPE=CHOICE_TYPES[CHOICE]
      RESPONSE_CHOICE=random.choice(CHOICE_TYPE)
      
      EMBED_COLOR=EMBED_COLORS[CHOICE]

      choice_embed.color=EMBED_COLOR
      choice_embed.description=RESPONSE_CHOICE
      #choice_embed.set_thumbnail(url="https://discord.com/assets/0cfd4882c0646d504900c90166d80cf8.svg")
      
      await ctx.send(embed=choice_embed)

def setup(bot):
    bot.add_cog(RockBall(bot))