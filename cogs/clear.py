import discord
from discord.ext import commands

class clear(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def clear(self, ctx, amount=0):
    amount = amount+0
    if amount > 100:
      embed = discord.Embed(description="You cannot delete more than 100 messages.", color=0x2b2d31)
      embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
      await ctx.reply(embed=embed, mention_author=False)
    else:
      await ctx.channel.purge(limit=amount)
      embed = discord.Embed(title="", description=f"✔️ Deleted {amount}/{amount} messages.", color=0x2b2d31)
      embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
      await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
  await client.add_cog(clear(client))