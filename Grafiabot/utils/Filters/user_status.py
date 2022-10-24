from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from Bestie_Robot import OPERATORS, dp
from Bestie_Robot.config import get_int_key
from Bestie_Robot.modules.utils.language import get_strings_dec
from Bestie_Robot.modules.utils.user_details import is_user_admin
from Bestie_Robot.services.mongo import mongodb


class IsAdmin(BoundFilter):
    key = "is_admin"

    def __init__(self, is_admin):
        self.is_admin = is_admin

    @get_strings_dec("global")
    async def check(self, event, strings):

        if hasattr(event, "message"):
            chat_id = event.message.chat.id
        else:
            chat_id = event.chat.id

        if not await is_user_admin(chat_id, event.from_user.id):
            task = event.answer if hasattr(event, "message") else event.reply
            await task(strings["u_not_admin"])
            return False
        return True


class IsOwner(BoundFilter):
    key = "is_owner"

    def __init__(self, is_owner):
        self.is_owner = is_owner

    async def check(self, message: types.Message):
        if message.from_user.id == get_int_key("OWNER_ID"):
            return True


class IsOP(BoundFilter):
    key = "is_op"

    def __init__(self, is_op):
        self.is_owner = is_op

    async def check(self, message: types.Message):
        if message.from_user.id in OPERATORS:
            return True


class NotGbanned(BoundFilter):
    key = "not_gbanned"

    def __init__(self, not_gbanned):
        self.not_gbanned = not_gbanned

    async def check(self, message: types.Message):
        check = mongodb.blacklisted_users.find_one({"user": message.from_user.id})
        if not check:
            return True


dp.filters_factory.bind(IsAdmin)
dp.filters_factory.bind(IsOwner)
dp.filters_factory.bind(NotGbanned)
dp.filters_factory.bind(IsOP)
