import discord
from discord.ext import commands

class ban(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, user: discord.Member, *, reason="None"):
      await user.ban(reason=reason)
      embed = discord.Embed(description=f"**{user}** has ben banned. \nReason = **{reason}**", color=0x2b2d31)
      embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
      await ctx.send(embed=embed)

async def setup(client):
  await client.add_cog(ban(client))