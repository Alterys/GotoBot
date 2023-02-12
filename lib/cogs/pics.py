from discord import Embed
from discord.ext.commands import Cog, command
from data.utils.utils import TAGS
import requests


class Pics(Cog):

    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    async def send_pic(ctx, api_url):
        response = requests.get(api_url)
        if response.status_code == 200:
            payload = response.json()
            embed = Embed()
            embed.set_image(url=payload['url'])
            await ctx.send(embed=embed)
        else:
            await ctx.send(embed=Embed(
                title='Не удалось получить вайфу. Пожалуйста, повторите попытку позже',
                color=0x36393e))

    @command(name="pics")
    async def pics(self, ctx, argument):
        slug = TAGS.get(argument, False)
        if slug:
            await self.send_pic(ctx, "https://api.waifu.pics/sfw"+slug)
        else:
            await ctx.send(embed=Embed(
                title='Данная категория не существует',
                color=0x36393e))


async def setup(bot):
    await bot.add_cog(Pics(bot))
