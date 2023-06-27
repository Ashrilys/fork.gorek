import discord
from discord.ext import commands

class mc(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["mc"])
  async def membercount(self, ctx):
    embed = discord.Embed(description=f"**{ctx.guild.name}** have `{ctx.guild.member_count}` members.", color=0x2b2d31)
    embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
    await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
  await client.add_cog(mc(client))