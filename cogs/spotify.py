import discord
from discord.ext import commands
from discord import Spotify

class sp(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["sp"])
  async def spotify(self, ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
        pass
    if user.activities:
        for activity in user.activities:
            if isinstance(activity, Spotify):
                embed = discord.Embed(
                    title=f"{user.name}'s listening to...",
                    color=0x2b2d31)
                embed.set_thumbnail(url=activity.album_cover_url)
                embed.add_field(name="Track:", value="{}".format(activity.title), inline=False)
                embed.add_field(name="Artist:", value=activity.artist, inline=False)
                embed.add_field(name="Album:", value=activity.album, inline=False)
                embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
                await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
  await client.add_cog(sp(client))