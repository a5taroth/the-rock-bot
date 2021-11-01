import discord
import random

from discord.ext import commands
from packages import responses

CHOICE_TYPE=["n", "p", "c"]

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
      
      NPC_CHOICE=random.choice(CHOICE_TYPE)
      if NPC_CHOICE=='n':
          responses.choice=random.choice(responses.neg)
          choice_embed.color=discord.Color.red()
      elif NPC_CHOICE=='p':
          responses.choice=random.choice(responses.pos)
          choice_embed.color=discord.Color.green()
      elif NPC_CHOICE=='c':
          responses.choice=random.choice(responses.non_com)
          choice_embed.color=discord.Color.gold()

      choice_embed.description=responses.choice
      #choice_embed.set_thumbnail(url="https://discord.com/assets/0cfd4882c0646d504900c90166d80cf8.svg")
      
      await ctx.send(embed=choice_embed)

def setup(bot):
    bot.add_cog(RockBall(bot))