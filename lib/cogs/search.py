import discord
from discord.ext.commands import Cog, command
from googleapiclient.discovery import build
from lib.bot import API_KEY, SEARCH_ENGINE_ID


class Search(Cog):

    def __init__(self, bot):
        self.bot = bot

    @command(name="s")
    async def search(self, ctx, *args):
        if not args:
            await ctx.send(embed=discord.Embed(title='!s <запрос>', color=0x36393e))
            return
        results = self.google_search(' '.join(args), API_KEY, SEARCH_ENGINE_ID, num=3)
        for result in results:
            await ctx.send(embed=discord.Embed(
                title=result['title'],
                url=result['link'],
                description=result['snippet'],
                color=0x36393e
            )
            )

    @staticmethod
    def google_search(search_term, api_key, cse_id, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        return res['items']


async def setup(bot):
    await bot.add_cog(Search(bot))
