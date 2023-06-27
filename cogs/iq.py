import discord
from discord.ext import commands
import random

class iq(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(pass_context=True)
  async def iq(self, ctx,):
    embed = discord.Embed(description=f"`🥸` You have `{random.randint(1, 251)}` iq.", color=0x2b2d31)
    embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
    await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
  await client.add_cog(iq(client))