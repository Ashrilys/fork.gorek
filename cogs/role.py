import discord
from discord.ext import commands

class role(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["ar", "awans"])
  @commands.has_permissions(manage_roles=True)
  async def addrole(self, ctx, user: discord.Member, *, role: discord.Role):
        if role in user.roles:
            embed = discord.Embed(title="", description=f"{user.mention} already has the role: **{role}**.", color=0x2b2d31)
            embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
            await ctx.send(embed=embed)
        else:
            await user.add_roles(role)
            embed = discord.Embed(title="", description=f"Added **{role.mention}** to {user.mention}.", color=0x2b2d31)
            embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
            await ctx.reply(embed=embed, mention_author=False)

  @commands.command(aliases=["rr", "degrad"])
  @commands.has_permissions(manage_roles=True)
  async def removerole(self, ctx, user: discord.Member, *, role: discord.Role):
        if role in user.roles:
            await user.remove_roles(role)
            embed = discord.Embed(title="", description=f"Removed **{role.mention}** from {user.mention}.", color=0x2b2d31)
            embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="", description=f"{user.mention} does not have the role: **{role.mention}**.", color=0x2b2d31)
            embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
            await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
  await client.add_cog(role(client))