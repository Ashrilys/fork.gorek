import discord
from discord.ext import commands
import random

class coin(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["flip", "cf", "coinflip"])
  async def coin(self, ctx):
   response = [
    "heads",
    "tails"
   ]
   embed = discord.Embed(description=f"`🪙` I choose `{random.choice(response)}`.", color=0x2b2d31)
   embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
   await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
  await client.add_cog(coin(client))