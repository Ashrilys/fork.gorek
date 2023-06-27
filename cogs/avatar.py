import discord
from discord.ext import commands
from discord.ui import Button, View

class av(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["av"])
  async def avatar(self, ctx, *, member: discord.Member = None):
     member = ctx.author if not member else member
     buttonav = Button(label="Download", style=discord.ButtonStyle.link, url=f"{member.avatar}")
     view = View()
     view.add_item(buttonav)
     embed = discord.Embed(title=f"{ctx.author.name}'s Avatar",
                            color=0x2b2d31)
     embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
     embed.set_image(url=member.avatar)
     await ctx.reply(embed=embed, mention_author=False, view=view)

async def setup(client):
  await client.add_cog(av(client))