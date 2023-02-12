from discord import Intents, Status, Activity, ActivityType, TextChannel
from discord.errors import Forbidden, HTTPException
from discord.ext.commands import Bot as DisBot
from discord.ext.commands import CommandNotFound, BadArgument, CommandOnCooldown
from discord.ext.commands import MissingPermissions, MissingRequiredArgument
from discord.ext.commands import when_mentioned_or

from ..db import db

OWNER_IDS = [694138142923685998, 327062541438287872]
COGS = ['search', 'pics']


def get_prefix(bot, message):
    return "!"


class Bot(DisBot):

    def __init__(self):
        super().__init__(command_prefix=get_prefix, owner_ids=OWNER_IDS, intents=Intents.all())

    async def update_db(self):
        pass

    async def setup(self):
        print('  starting setup..')
        for cog in COGS:
            await DisBot.load_extension(self, f"lib.cogs.{cog}")
            print(f"    {cog}_cog loaded..")
        print('  setup finished..')

    async def on_connect(self):
        print("bot connect")
        await self.setup()

    async def on_error(self, event_method, *args, **kwargs):
        if event_method == "on_command_error":
            pass
        else:
            pass
        raise

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            await ctx.send("Команда не найдена.")
        elif isinstance(exc, MissingPermissions):
            await ctx.send("У тебя недостаточно прав использовать эту команду!")
        elif isinstance(exc, MissingRequiredArgument):
            await ctx.send("Добавь необходимые аргументы!")
        elif isinstance(exc, BadArgument):
            await ctx.send("Ты ввел что-то неверно, попробуй ещё раз.")
        elif hasattr(exc, "original"):
            if isinstance(exc.original, HTTPException):
                pass
            elif isinstance(exc.original, Forbidden):
                await ctx.send("У меня нет на это разрешения")
        elif hasattr(exc, "original"):
            raise exc.original
        else:
            raise exc

    async def on_ready(self):
        await self.update_db()
        await self.change_presence(activity=Activity(name="", type=ActivityType.listening))
        print("bot ready..")


bot = Bot()
