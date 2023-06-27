import discord
from discord.ext import commands

class ui(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["ui"])
  async def userinfo(self, ctx, user: discord.Member = None):

    if user == None:
        user = ctx.author

    rlist = []
    for role in user.roles:
      if role.name != "@everyone":
        rlist.append(role.mention)

    b = ", ".join(rlist)

    embed = discord.Embed(title="About user", color=0x2b2d31)
    embed.set_thumbnail(url=user.avatar),
    embed.add_field(name="General:", value=f"**Name:** {user.mention} \n**ID:** `{user.id}`\n**Bot?:** `{user.bot}`", inline=False)
    embed.add_field(name="Dates:", value=f"**Created at:** `{user.created_at.__format__('%A, %d. %B %Y')}` \n**Joined at:** `{user.joined_at.__format__('%A, %d. %B %Y')}`", inline=False)
    embed.add_field(name="Roles Info:", value=f"**Top Role:** {user.top_role.mention} \n  **Roles ({len(rlist)}):** {''.join([b])}", inline=False)
    embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
    await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
  await client.add_cog(ui(client))