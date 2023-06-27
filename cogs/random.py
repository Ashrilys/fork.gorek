import discord
from discord.ext import commands
import random

class rd(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def random(self, ctx):
    embed = discord.Embed(description=f"Your random number is `{random.randrange(100)}`.", color=0x2b2d31)
    embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
    await ctx.reply(embed=embed, mention_author=False)
    

async def setup(client):
  await client.add_cog(rd(client))