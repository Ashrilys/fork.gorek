import discord
from discord.ext import commands
import sqlite3

class prefix(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def prefix(self, ctx, prefix):
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT guild_id FROM info WHERE guild_id = {ctx.author.guild.id}")
    wynik = cursor.fetchone()
    if wynik is None:
      cursor.execute("INSERT INTO info(guild_id, prefix) VALUES(?, ?)", (ctx.author.guild.id, prefix))
    else:
      cursor.execute("UPDATE info SET prefix = ? WHERE guild_id = ?", (prefix, ctx.author.guild.id))
      embed = discord.Embed(description=f"Prefix changed to `{prefix}`", color=0x2b2d31)
      embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
      await ctx.reply(embed=embed, mention_author=False)
      db.commit()
      cursor.close()
      db.close()

  @commands.Cog.listener()
  async def on_message(self, message: discord.Message):
    if message.content == f"<@{self.client.user.id}>":
     db = sqlite3.connect("data.db")
     cursor = db.cursor()
     cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {message.author.guild.id}")
     wynik = cursor.fetchone()
    if wynik == None:
     prefix = ";"
    else:
     prefix = wynik[0]  
     await message.reply(f"My prefix here is: **`{prefix}`**", mention_author=False)
     db.commit()
     cursor.close()
     db.close()
      

async def setup(client):
  await client.add_cog(prefix(client))