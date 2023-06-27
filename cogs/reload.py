import discord
from discord.ext import commands
from discord import permissions
from discord.ext.commands import Bot, is_owner

class rl(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["r"])
  @is_owner()
  async def reload(self, ctx, name: str):
    try:
      await self.client.reload_extension(f"cogs.{name}")
    except Exception as e:
      return await ctx.send(default.trackback_maker(e))
    embed = discord.Embed(description=f"Reloaded `{name}.py`", color=0x2b2d31)
    embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
    await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
  await client.add_cog(rl(client))