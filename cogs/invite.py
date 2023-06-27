import discord
from discord.ext import commands
from discord.ui import Button, View

class invite(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["i"])
  async def invite(self, ctx):
    button = Button(label="Invite Me", style=discord.ButtonStyle.link, url="PUT THERE BOT INVITE URL")
    view = View()
    view.add_item(button)
    embed = discord.Embed(description = "If you want, you can invite bot to your server.", color=0x2b2d31)
    embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
    await ctx.reply(embed=embed, view=view, mention_author=False)

async def setup(client):
  await client.add_cog(invite(client))