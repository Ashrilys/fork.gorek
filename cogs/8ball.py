import discord
from discord.ext import commands
import random

class eightball(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["8ball", "8b"])
  async def eightball(self, ctx, *, question):
   response = [
    "Yes",
    "No",
    "Maybe",
    "I don't know",
    "Perhaps",
    "Sure",
    "For sure yes",
    "Of course not",
    "In 10 minutes",
    "Tomorrow",
    "Today",
    "As I see it, yes",
    "Positive",
    "From my point of view, yes",
    "Convinced",
    "Most Likley",
    "Chances High",
    "Negative",
    "Not Convinced",
    "Not Sure",
    "I cannot predict now",
    "Im to lazy to predict",
    "I am tired. *proceeds with sleeping*"
  ]
   embed = discord.Embed(description=f"`🔮` **Question:** {question}\n`🔮` **Answer:** {random.choice(response)}.", color=0x2b2d31)
   embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar)
   await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
  await client.add_cog(eightball(client))