import discord
from discord.ext import commands

class reaction(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["react"])
  @commands.has_permissions(manage_messages=True)
  async def reaction(self, msg: discord.Message, reaction):
    await msg.add_reaction(reaction)

async def setup(client):
  await client.add_cog(reaction(client))