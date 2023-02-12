import discord
from discord.ext.commands import Cog, command


class Help(Cog):

    def __init__(self, bot):
        self.bot = bot


async def setup(bot):
    await bot.add_cog(Help(bot))
