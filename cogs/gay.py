import discord
from discord.ext import commands
import random

class gay(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(pass_context=True, aliases=["gay"])
  async def howgay(self, ctx):
    embed = discord.Embed(description=f"`🏳️‍🌈` You are `{random.randint(1, 100)}%` gay.", color=0x2b2d31)
    embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
    await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
  await client.add_cog(gay(client))