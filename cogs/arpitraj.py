import discord
from discord import activity
from discord.ext import commands

class arpitraj(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def whatfileisthis(self, ctx):
        await ctx.send("this file is arpitraj.py")

    @commands.command()
    async def whatfileisnotthis(self, ctx):
        await ctx.send("this file is not bagai.py")

async def setup(bot):
    await bot.add_cog(arpitraj(bot))
