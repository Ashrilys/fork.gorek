import discord
from discord.ext import commands


class google(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["search"])
  async def google(self, ctx, *, msg):
      msg = msg.replace(" ", "+")
      await ctx.reply(f"https://www.google.com/search?q={msg}", mention_author=False)

async def setup(client):
  await client.add_cog(google(client))