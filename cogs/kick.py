import discord
from discord.ext import commands

class kick(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, user: discord.Member, *, reason="None"):
      await user.kick(reason=reason)
      embed = discord.Embed(description=f"**{user}** has ben kicked. \nReason = **{reason}**", color=0x2b2d31)
      embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
      await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
  await client.add_cog(kick(client))