import discord
from discord import activity
from discord.ext import commands

class test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == "hello":
            await msg.reply("kill yourself :stuck_out_tongue_winking_eye:")

    @commands.command()
    async def test(self, ctx):
        await ctx.send("poop")


async def setup(bot):
    await bot.add_cog(test(bot))
