from asyncio.tasks import wait
import discord
from discord.ext import commands
import os
import sqlite3

def get_prefix(client, message):
  db = sqlite3.connect("data.db")
  cursor = db.cursor()
  cursor.execute(f"SELECT prefix FROM info WHERE guild_id = {message.guild.id}")
  wynik = cursor.fetchone()
  if wynik is None:
     prefix = ";"
  else:
     prefix = wynik
  cursor.close()
  db.close()
  return prefix

intents = discord.Intents.all()
client = commands.Bot(command_prefix=get_prefix, intents=intents)

client.remove_command('help')

@client.event
async def setup_hook():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            await client.load_extension(f"cogs.{file[:-3]}")

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(description="`📦` You didn't provide an argument.", color=0x2b2d31)
    embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
    await ctx.reply(embed=embed, mention_author=False)
  elif isinstance(error, commands.CommandNotFound):
    embed = discord.Embed(description="`❓` Command not found.", color=0x2b2d31)
    embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
    await ctx.reply(embed=embed, mention_author=False)
  elif isinstance(error, commands.MissingPermissions):
    embed = discord.Embed(description="`🔨` You do not have permission to use this command.", color=0x2b2d31)
    embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
    await ctx.reply(embed=embed, mention_author=False)

@client.event
async def on_ready():
  db = sqlite3.connect("data.db")
  cursor = db.cursor()
  cursor.execute("CREATE TABLE IF NOT EXISTS info(guild_id INT, prefix STR)")
  cursor.close()
  db.close()
  print(f"{client.user.name} working!")
  await client.change_presence(activity=discord.Game(name=f";help"))


client.run("PUT THERE BOT TOKEN")