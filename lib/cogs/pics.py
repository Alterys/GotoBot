import discord
from discord.ext.commands import Cog, command
import requests


class Pics(Cog):

    def __init__(self, bot):
        self.bot = bot
        self.tags = {'waifu': "/waifu", 'neko': "/neko", 'shinobu': '/shinobu', 'megumin': '/megumin',
                     'bully': '/bully', 'cuddle': '/cuddle', 'cry': '/cry', 'hug': '/hug', 'awoo': '/awoo',
                     'kiss': '/kiss', 'lick': '/lick', 'pat': '/pat', 'smug': '/smug', 'bonk': '/bonk', 'yeet': '/yeet',
                     'blush': '/blush', 'smile': '/smile', 'wave': '/wave', 'highfive': '/highfive',
                     'handhold': '/handhold', 'nom': '/nom', 'bite': '/bite', 'glomp': '/glomp', 'slap': '/slap',
                     'kill': '/kill', 'kick': '/kick', 'happy': '/happy', 'wink': '/wink', 'poke': '/poke',
                     'dance': '/dance', 'cringe': '/cringe'}

    @staticmethod
    async def send_pic(ctx, api_url):
        response = requests.get(api_url)
        if response.status_code == 200:
            payload = response.json()
            embed = discord.Embed()
            embed.set_image(url=payload['url'])
            await ctx.send(embed=embed)
        else:
            await ctx.send(embed=discord.Embed(
                title='Не удалось получить вайфу. Пожалуйста, повторите попытку позже',
                color=0x36393e))

    @command(name="pics")
    async def pics(self, ctx, argument):
        slug = self.tags.get(argument, False)
        if slug:
            await self.send_pic(ctx, "https://api.waifu.pics/sfw"+slug)
        else:
            await ctx.send(embed=discord.Embed(
                title='Данная категория не существует',
                color=0x36393e))


async def setup(bot):
    await bot.add_cog(Pics(bot))
