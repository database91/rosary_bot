import asyncio

from aiogram import F
from aiogram.filters.magic_data import MagicFilter
from aiogram import Bot, Dispatcher, types
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import CommandStart




bot = Bot(token="8461458090:AAFeGNfdtGMRH0z18Efsg1EaO9wL_oGHZIA")

dp = Dispatcher()


@dp.message(CommandStart())
async def start_func(message: types.Message):
    text = "<b>Привествую вас!</b> В нашем боте!  --&#9899--"
    await message.answer(text=text,parse_mode=ParseMode.HTML)      

@dp.message(F.photo)
async def photo(message: types.Message):
    var_text_two = 'ЭТО ТЕКСТ ВТОРОЙ ПЕРЕМЕННОЙ'
    var_text = f"это просто прикольная переменная с f строкой {var_text_two}"
    await message.answer(text=var_text)

async def main():
    #пропускает апдейты когда выключен.
    await bot.delete_webhook(drop_pending_updates=True)
    #добавляем в бота кнопку меню
    #запускает бота в поллинг режиме
    await dp.start_polling(bot)

#это команда запускает бота ( не забывай про библиотеку asyncio)
if __name__ == "__main__":
    asyncio.run(main())