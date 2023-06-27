import discord
from discord.ext import commands
from discord.ui import Button, View
import sqlite3

class h(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.group(name="help", invoke_without_command=True, aliases=["h"])
  async def help(self, ctx):
   db = sqlite3.connect("data.db")
   cursor = db.cursor()
   cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {ctx.author.guild.id}")
   wynik = cursor.fetchone()
   if wynik == None:
    prefix = ";"
   else:
     prefix = wynik[0]
   embed = discord.Embed(
    title="Help",
    description=
    f"To see information about a command, type `{prefix}help <cmd>`. \n` <> ` - This means the argument is required. \n` [] ` - This means the argument is optional.",
    color=0x2b2d31)
   embed.add_field(name="Bot:", value="`help`, `botinfo`, `invite`,")
   embed.add_field(name="Another:", value="`serverinfo`, `userinfo`, `ping`, `avatar`, `membercount`, `spotify`,", inline=False)
   embed.add_field(name="Music:", value="`Working...`", inline=False)
   embed.add_field(name="Fun:", value="`8ball`, `iq`, `coin`, `howgay`, `howcool`, `random`, `wiki`, `google`,", inline=False)
   embed.add_field(name="Moderation:", value="`ban`, `kick`, `clear`, `addrole`, `removerole`, `reaction`, `prefix`,", inline=False)
   embed.add_field(name="Developer:", value="`reload`,")
   embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
   await ctx.reply(embed=embed, mention_author=False)
   db.commit()
   cursor.close()
   db.close()

  @help.command(aliases=["help-test"])
  async def test(self, ctx):
      db = sqlite3.connect("data.db")
      cursor = db.cursor()
      cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {ctx.author.guild.id}")
      wynik = cursor.fetchone()
      if wynik == None:
       prefix = ";"
      else:
       prefix = wynik[0]
       embed = discord.Embed(title="Help: test", description=f"Test. \n\n**How to use:** \n```{prefix}test``` \n**Aliases:** \n```None```", color=0x2b2d31)
       await ctx.reply(embed=embed, mention_author=False)
       db.commit()
       cursor.close()
       db.close()

  @help.command(aliases=["help-ban"])
  async def ban(self, ctx):
      db = sqlite3.connect("data.db")
      cursor = db.cursor()
      cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {ctx.author.guild.id}")
      wynik = cursor.fetchone()
      if wynik == None:
       prefix = ";"
      else:
       prefix = wynik[0]
      embed = discord.Embed(title="Help: ban", description=f"Bans the user. \n\n**How to use:** \n```{prefix}ban <user> [reason]``` \n**Aliases:** \n```None```", color=0x2b2d31)
      await ctx.reply(embed=embed, mention_author=False)
      db.commit()
      cursor.close()
      db.close()

  @help.command(aliases=["help-kick"])
  async def kick(self, ctx):
      db = sqlite3.connect("data.db")
      cursor = db.cursor()
      cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {ctx.author.guild.id}")
      wynik = cursor.fetchone()
      if wynik == None:
       prefix = ";"
      else:
       prefix = wynik[0]
      embed = discord.Embed(title="Help: kick", description=f"Kicks the user. \n\n**How to use:** \n```{prefix}kick <user> [reason]``` \n**Aliases:** \n```None```", color=0x2b2d31)
      await ctx.reply(embed=embed, mention_author=False)
      db.commit()
      cursor.close()
      db.close()

  @help.command(aliases=["help-iq"])
  async def iq(self, ctx):
      db = sqlite3.connect("data.db")
      cursor = db.cursor()
      cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {ctx.author.guild.id}")
      wynik = cursor.fetchone()
      if wynik == None:
       prefix = ";"
      else:
       prefix = wynik[0]
      embed = discord.Embed(title="Help: iq", description=f"The bot tells you how much iq you have. \n\n**How to use:** \n```{prefix}iq``` \n**Aliases:** \n```None```", color=0x2b2d31)
      await ctx.reply(embed=embed, mention_author=False)
      db.commit()
      cursor.close()
      db.close()

  @help.command(aliases=["help-coin"])
  async def coin(self, ctx):
      db = sqlite3.connect("data.db")
      cursor = db.cursor()
      cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {ctx.author.guild.id}")
      wynik = cursor.fetchone()
      if wynik == None:
       prefix = ";"
      else:
       prefix = wynik[0]
      embed = discord.Embed(title="Help: coin", description=f"The bot flips a coin. \n\n**How to use:** \n```{prefix}coin``` \n**Aliases:** \n```None```", color=0x2b2d31)
      await ctx.reply(embed=embed, mention_author=False)
      db.commit()
      cursor.close()
      db.close()

  @help.command(aliases=["help-ping"])
  async def ping(self, ctx):
      db = sqlite3.connect("data.db")
      cursor = db.cursor()
      cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {ctx.author.guild.id}")
      wynik = cursor.fetchone()
      if wynik == None:
       prefix = ";"
      else:
       prefix = wynik[0]
      embed = discord.Embed(title="Help: ping", description=f"The bot shows you information about the ping. \n\n**How to use:** \n```{prefix}ping``` \n**Aliases:** \n```None```", color=0x2b2d31)
      await ctx.reply(embed=embed, mention_author=False)
      db.commit()
      cursor.close()
      db.close()

  @help.command(aliases=["help-serverinfo", "help-si"])
  async def serverinfo(self, ctx):
      db = sqlite3.connect("data.db")
      cursor = db.cursor()
      cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {ctx.author.guild.id}")
      wynik = cursor.fetchone()
      if wynik == None:
       prefix = ";"
      else:
       prefix = wynik[0]
      embed = discord.Embed(title="Help: serverinfo", description=f"The bot shows you information about the server. \n\n**How to use:** \n```{prefix}serverinfo``` \n**Aliases:** \n```{prefix}si```", color=0x2b2d31)
      await ctx.reply(embed=embed, mention_author=False)
      db.commit()
      cursor.close()
      db.close()

  @help.command(aliases=["help-botinfo", "help-bi"])
  async def botinfo(self, ctx):
      db = sqlite3.connect("data.db")
      cursor = db.cursor()
      cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {ctx.author.guild.id}")
      wynik = cursor.fetchone()
      if wynik == None:
       prefix = ";"
      else:
       prefix = wynik[0]
      embed = discord.Embed(title="Help: botinfo", description=f"The bot shows you information about the bot. \n\n**How to use:** \n```{prefix}botinfo``` \n**Aliases:** \n```{prefix}bi```", color=0x2b2d31)
      await ctx.reply(embed=embed, mention_author=False)
      db.commit()
      cursor.close()
      db.close()

  @help.command(aliases=["help-userinfo", "help-ui"])
  async def userinfo(self, ctx):
      db = sqlite3.connect("data.db")
      cursor = db.cursor()
      cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {ctx.author.guild.id}")
      wynik = cursor.fetchone()
      if wynik == None:
       prefix = ";"
      else:
       prefix = wynik[0]
      embed = discord.Embed(title="Help: userinfo", description=f"The bot shows you information about the user. \n\n**How to use:** \n```{prefix}userinfo [user]``` \n**Aliases:** \n```{prefix}ui```", color=0x2b2d31)
      await ctx.reply(embed=embed, mention_author=False)
      db.commit()
      cursor.close()
      db.close()

  @help.command(aliases=["help-avatar"])
  async def avatar(self, ctx):
      db = sqlite3.connect("data.db")
      cursor = db.cursor()
      cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {ctx.author.guild.id}")
      wynik = cursor.fetchone()
      if wynik == None:
       prefix = ";"
      else:
       prefix = wynik[0]
      embed = discord.Embed(title="Help: avatar", description=f"The bot sends the user's avatar. \n\n**How to use:** \n```{prefix}avatar [user]``` \n**Aliases:** \n```{prefix}av```", color=0x2b2d31)
      await ctx.reply(embed=embed, mention_author=False)
      db.commit()
      cursor.close()
      db.close()

  @help.command(aliases=["help-clear"])
  async def clear(self, ctx):
      db = sqlite3.connect("data.db")
      cursor = db.cursor()
      cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {ctx.author.guild.id}")
      wynik = cursor.fetchone()
      if wynik == None:
       prefix = ";"
      else:
       prefix = wynik[0]
      embed = discord.Embed(title="Help: clear", description=f"The bot deletes messages. \n\n**How to use:** \n```{prefix}clear <amount>``` \n**Aliases:** \n```None```", color=0x2b2d31)
      await ctx.reply(embed=embed, mention_author=False)
      db.commit()
      cursor.close()
      db.close()

  @help.command(aliases=["help-addrole"])
  async def addrole(self, ctx):
      db = sqlite3.connect("data.db")
      cursor = db.cursor()
      cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {ctx.author.guild.id}")
      wynik = cursor.fetchone()
      if wynik == None:
       prefix = ";"
      else:
       prefix = wynik[0]
      embed = discord.Embed(title="Help: addrole", description=f"The bot gives the user a role. \n\n**How to use:** \n```{prefix}addrole <user> <role>``` \n**Aliases:** \n```{prefix}ar```", color=0x2b2d31)
      await ctx.reply(embed=embed, mention_author=False)
      db.commit()
      cursor.close()
      db.close()

  @help.command(aliases=["help-removerole"])
  async def removerole(self, ctx):
      db = sqlite3.connect("data.db")
      cursor = db.cursor()
      cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {ctx.author.guild.id}")
      wynik = cursor.fetchone()
      if wynik == None:
       prefix = ";"
      else:
       prefix = wynik[0]
      embed = discord.Embed(title="Help: removerole", description=f"The bot remove the user a role. \n\n**How to use:** \n```{prefix}removerole <user> <role>``` \n**Aliases:** \n```{prefix}rr```", color=0x2b2d31)
      await ctx.reply(embed=embed, mention_author=False)
      db.commit()
      cursor.close()
      db.close()

  @help.command(aliases=["react"])
  async def reaction(self, ctx):
      db = sqlite3.connect("data.db")
      cursor = db.cursor()
      cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {ctx.author.guild.id}")
      wynik = cursor.fetchone()
      if wynik == None:
       prefix = ";"
      else:
       prefix = wynik[0]
      embed = discord.Embed(title="Help: reaction", description=f"The bot adds an emoji to the message. \n\n**How to use:** \n```{prefix}reaction <msg id> <emoji>``` \n**Aliases:** \n```{prefix}react```", color=0x2b2d31)
      await ctx.reply(embed=embed, mention_author=False)
      db.commit()
      cursor.close()
      db.close()

  @help.command(aliases=["wikipedia"])
  async def wiki(self, ctx):
      db = sqlite3.connect("data.db")
      cursor = db.cursor()
      cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {ctx.author.guild.id}")
      wynik = cursor.fetchone()
      if wynik == None:
       prefix = ";"
      else:
       prefix = wynik[0]
      embed = discord.Embed(title="Help: wikipedia", description=f"The bot searches for the given information on the wikipedia. \n\n**How to use:** \n```{prefix}wikipedia <text>``` \n**Aliases:** \n```{prefix}wiki```", color=0x2b2d31)
      await ctx.reply(embed=embed, mention_author=False)
      db.commit()
      cursor.close()
      db.close()

  @help.command(aliases=["help-google"])
  async def google(self, ctx):
      db = sqlite3.connect("data.db")
      cursor = db.cursor()
      cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {ctx.author.guild.id}")
      wynik = cursor.fetchone()
      if wynik == None:
       prefix = ";"
      else:
       prefix = wynik[0]
      embed = discord.Embed(title="Help: google", description=f"The bot searches for the given information on the google. \n\n**How to use:** \n```{prefix}google <text>``` \n**Aliases:** \n```None```", color=0x2b2d31)
      await ctx.reply(embed=embed, mention_author=False)
      db.commit()
      cursor.close()
      db.close()

  @help.command(aliases=["help-invite"])
  async def invite(self, ctx):
      db = sqlite3.connect("data.db")
      cursor = db.cursor()
      cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {ctx.author.guild.id}")
      wynik = cursor.fetchone()
      if wynik == None:
       prefix = ";"
      else:
       prefix = wynik[0]
      embed = discord.Embed(title="Help: invite", description=f"The bot sends its link to be added to the server. \n\n**How to use:** \n```{prefix}invite``` \n**Aliases:** \n```None```", color=0x2b2d31)
      await ctx.reply(embed=embed, mention_author=False)
      db.commit()
      cursor.close()
      db.close()

  @help.command(aliases=["r"])
  async def reload(self, ctx):
      db = sqlite3.connect("data.db")
      cursor = db.cursor()
      cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {ctx.author.guild.id}")
      wynik = cursor.fetchone()
      if wynik == None:
       prefix = ";"
      else:
       prefix = wynik[0]
      embed = discord.Embed(title="Help: reload", description=f"A command that helps the *owner* reload files. \n\n**How to use:** \n```{prefix}reload <file>``` \n**Aliases:** \n```{prefix}r```", color=0x2b2d31)
      await ctx.reply(embed=embed, mention_author=False)
      db.commit()
      cursor.close()
      db.close()

  @help.command(aliases=["gay"])
  async def howgay(self, ctx):
      db = sqlite3.connect("data.db")
      cursor = db.cursor()
      cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {ctx.author.guild.id}")
      wynik = cursor.fetchone()
      if wynik == None:
       prefix = ";"
      else:
       prefix = wynik[0]
      embed = discord.Embed(title="Help: howgay", description=f"The bot shows you how gay you are. \n\n**How to use:** \n```{prefix}howgay``` \n**Aliases:** \n```{prefix}gay```", color=0x2b2d31)
      await ctx.reply(embed=embed, mention_author=False)
      db.commit()
      cursor.close()
      db.close()

  @help.command(aliases=["cool"])
  async def howcool(self, ctx):
      db = sqlite3.connect("data.db")
      cursor = db.cursor()
      cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {ctx.author.guild.id}")
      wynik = cursor.fetchone()
      if wynik == None:
       prefix = ";"
      else:
       prefix = wynik[0]
      embed = discord.Embed(title="Help: howcool", description=f"The bot shows you how cool you are. \n\n**How to use:** \n```{prefix}howcool``` \n**Aliases:** \n```{prefix}cool```", color=0x2b2d31)
      await ctx.reply(embed=embed, mention_author=False)
      db.commit()
      cursor.close()
      db.close()

  @help.command(aliases=["help-random"])
  async def random(self, ctx):
      db = sqlite3.connect("data.db")
      cursor = db.cursor()
      cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {ctx.author.guild.id}")
      wynik = cursor.fetchone()
      if wynik == None:
       prefix = ";"
      else:
       prefix = wynik[0]
      embed = discord.Embed(title="Help: random", description=f"The bot draws a number from 0 to 100. \n\n**How to use:** \n```{prefix}random``` \n**Aliases:** \n```None```", color=0x2b2d31)
      await ctx.reply(embed=embed, mention_author=False)
      db.commit()
      cursor.close()
      db.close()

  @help.command(aliases=["mc"])
  async def membercount(self, ctx):
      db = sqlite3.connect("data.db")
      cursor = db.cursor()
      cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {ctx.author.guild.id}")
      wynik = cursor.fetchone()
      if wynik == None:
       prefix = ";"
      else:
       prefix = wynik[0]
      embed = discord.Embed(title="Help: membercount", description=f"The bot shows how many people are on the server. \n\n**How to use:** \n```{prefix}membercount``` \n**Aliases:** \n```{prefix}mc```", color=0x2b2d31)
      await ctx.reply(embed=embed, mention_author=False)
      db.commit()
      cursor.close()
      db.close()

  @help.command(aliases=["8ball", "8b"])
  async def eightball(self, ctx):
      db = sqlite3.connect("data.db")
      cursor = db.cursor()
      cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {ctx.author.guild.id}")
      wynik = cursor.fetchone()
      if wynik == None:
       prefix = ";"
      else:
       prefix = wynik[0]
      embed = discord.Embed(title="Help: 8ball", description=f"The bot answers your question. \n\n**How to use:** \n```{prefix}8ball <question>``` \n**Aliases:** \n```{prefix}8b, {prefix}eightball```", color=0x2b2d31)
      await ctx.reply(embed=embed, mention_author=False)
      db.commit()
      cursor.close()
      db.close()

  @help.command(aliases=["p"])
  async def prefix(self, ctx):
      db = sqlite3.connect("data.db")
      cursor = db.cursor()
      cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {ctx.author.guild.id}")
      wynik = cursor.fetchone()
      if wynik == None:
       prefix = ";"
      else:
       prefix = wynik[0]
      embed = discord.Embed(title="Help: prefix", description=f"Changes the bot prefix on the server. \n\n**How to use:** \n```{prefix}prefix <prefix>``` \n**Aliases:** \n```{prefix}p```", color=0x2b2d31)
      await ctx.reply(embed=embed, mention_author=False)
      db.commit()
      cursor.close()
      db.close()

  @help.command(aliases=["sp"])
  async def spotify(self, ctx):
      db = sqlite3.connect("data.db")
      cursor = db.cursor()
      cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {ctx.author.guild.id}")
      wynik = cursor.fetchone()
      if wynik == None:
       prefix = ";"
      else:
       prefix = wynik[0]
      embed = discord.Embed(title="Help: spotify", description=f"Check who listens to what on spotify. \n\n**How to use:** \n```{prefix}spotify [user]``` \n**Aliases:** \n```{prefix}sp```", color=0x2b2d31)
      await ctx.reply(embed=embed, mention_author=False)
      db.commit()
      cursor.close()
      db.close()

async def setup(client):
  await client.add_cog(h(client))