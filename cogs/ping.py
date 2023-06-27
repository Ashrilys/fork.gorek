import discord
from discord.ext import commands

class ping(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def ping(self, ctx):
    embed = discord.Embed(description=f"Ping: **`{round(self.client.latency * 1000)}ms`**.", color=0x2b2d31)
    embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
    await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
  await client.add_cog(ping(client))