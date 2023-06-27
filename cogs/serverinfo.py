import discord
from discord.ext import commands

class si(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["si"])
  async def serverinfo(self, ctx):
   owner = ctx.guild.owner_id
   embed = discord.Embed(title="About server", color=0x2b2d31)
   embed.add_field(name="General: ", value=f"**Server Owner:** <@{owner}>\n**ID:** `{ctx.guild.id}` \n**Name:** `{ctx.guild.name}`", inline=False)
   embed.add_field(name="Counts:", value=f"**Members:** `{ctx.guild.member_count}` \n**Roles:** `{len(ctx.message.guild.roles)}` \n**Text Channels:** `{len(ctx.message.guild.text_channels)}` \n**Voice Channels:** `{len(ctx.message.guild.voice_channels)}`", inline=False)
   embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
   await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
  await client.add_cog(si(client))