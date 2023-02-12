from discord.ext.commands import Cog
from data.utils.utils import ID_POST, ROLES_LIST, MAX_ROLES, USER_ROLES_LIST
from discord import utils


class Roles(Cog):

    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == ID_POST:
            channel = self.bot.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            user = utils.get(message.guild.members, id=payload.user_id)
            emoji = str(payload.emoji)

            try:
                role = utils.get(message.guild.roles, id=ROLES_LIST[emoji])

                if len([i for i in user.roles if i.id not in USER_ROLES_LIST]) <= MAX_ROLES:
                    await user.add_roles(role)
                    print(f"{user.name} получил роль {role.name}")
                else:
                    await message.remove_reaction(payload.emoji, user)
                    print(f"Ошибка! пользователь {user.name} пытался получить слишком много ролей")

            except Exception as _ex:
                print(repr(_ex))

    @Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        channel = self.bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = utils.get(message.guild.members, id=payload.user_id)
        try:
            emoji = str(payload.emoji)
            role = utils.get(message.guild.roles, id=ROLES_LIST[emoji])
            await user.remove_roles(role)
        except Exception as _ex:
            print(repr(_ex))


async def setup(bot):
    await bot.add_cog(Roles(bot))
