import discord
from discord.ext.commands import Cog, command
import requests


class Pics(Cog):

    def __init__(self, bot):
        self.bot = bot

    @command(name="pics")
    async def pics(self, ctx, argument):
        if argument == 'waifu':
            api_url = "https://api.waifu.pics/sfw/waifu"
            response = requests.get(api_url)
            if response.status_code == 200:
                payload = response.json()
                embed = discord.Embed()
                embed.set_image(url=payload['url'])
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=discord.Embed(
                    title='Не удалось получить вайфу. Пожалуйста, повторите попытку позже',
                    color=0x36393e
                )
                )


async def setup(bot):
    await bot.add_cog(Pics(bot))
