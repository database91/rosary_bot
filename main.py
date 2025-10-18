import asyncio


from aiogram import F
from aiogram.filters.magic_data import MagicFilter
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import CommandStart, Command
from kb.list_commands import listcom
from errors.erros import error_checker

#создаем экземпляр бота 
token = error_checker()
bot = Bot(token=token)

dp = Dispatcher()


@dp.message(CommandStart())
async def start_func(message: types.Message):
    text = "<b>Привествую вас!</b> В нашем боте! --&#9899--"
    await message.answer(text=text)      


@dp.message(Command("sorrowful_mystery", prefix="/"))
async def sorrows(message: types.Message):
    await message.answer("здесь будут скорбные тайный розария")
    

async def main():
    #пропускает апдейты когда выключен.
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=listcom)
    #запускает бота в поллинг режиме
    await dp.start_polling(bot)

#это команда запускает бота ( не забывай про библиотеку asyncio)
if __name__ == "__main__":
    asyncio.run(main())