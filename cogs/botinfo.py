import discord
from discord.ext import commands
from discord.ui import Button, View
import sqlite3

class bi(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["bi"])
  async def botinfo(self, ctx):
     embed = discord.Embed(title="About gorek", description=f"Gorek was created by **[xrbi](xrbi.netlify.app/)** \n\n**Prefix:** `;`, \n **Ping:** `{round(self.client.latency * 1000)}ms`, \n **Commands:** `27`, \n **Bot:** `{len(self.client.users)}` users on `{len(self.client.guilds)}` servers,", color=0x2b2d31)
     embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
     button1 = Button(label="Support", style=discord.ButtonStyle.link, url="DISCORD SERVER LINK")
     button2 = Button(label="Website", style=discord.ButtonStyle.link, url="WEBSITE LINK")
     view = View()
     view.add_item(button1)
     view.add_item(button2)
     await ctx.reply(embed=embed, mention_author=False, view=view)

async def setup(client):
  await client.add_cog(bi(client))