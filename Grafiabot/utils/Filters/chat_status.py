from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from Bestie_Robot import dp


class OnlyPM(BoundFilter):
    key = "only_pm"

    def __init__(self, only_pm):
        self.only_pm = only_pm

    async def check(self, message: types.Message):
        if message.from_user.id == message.chat.id:
            return True


class OnlyGroups(BoundFilter):
    key = "only_groups"

    def __init__(self, only_groups):
        self.only_groups = only_groups

    async def check(self, message: types.Message):
        if not message.from_user.id == message.chat.id:
            return True


dp.filters_factory.bind(OnlyPM)
dp.filters_factory.bind(OnlyGroups)
