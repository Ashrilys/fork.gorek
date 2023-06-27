import discord
from discord.ext import commands
import random

class cool(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["cool"])
  async def howcool(self, ctx):
    embed = discord.Embed(description=f"`😎` You are `{random.randrange(101)}%` cool.", color=0x2b2d31)
    embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
    await ctx.reply(embed=embed, mention_author=False)
    

async def setup(client):
  await client.add_cog(cool(client))