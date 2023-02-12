from discord.ext.commands import Cog


class Music(Cog):

    def __init__(self, bot):
        self.bot = bot


async def setup(bot):
    await bot.add_cog(Music(bot))
