import asyncio
import logging
from aiogram.types import *

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram import F

from config import TOKEN

#импорт ассетов
from commands import cmd_start as COMMANDS_cmd_start
from commands import cmd_conspekti as COMMANDS_cmd_conspekti


#-----------------------------------------------------------------
#session = AiohttpSession(proxy = 'http://proxy.server:3128')
#bot = Bot(token=TOKEN, session=session)
#-----------------------------------------------------------------
bot = Bot(token=TOKEN)
#-----------------------------------------------------------------


logging.basicConfig(level=logging.INFO)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    try:
        await COMMANDS_cmd_start.cmd_start(message)
    except:
        print("Command START(main.py) error", message)


@dp.message(F.text.lower() == "выход")
async def cmd_exit(message: types.Message):
    try:
        await COMMANDS_cmd_start.cmd_exit(message)
    except:
        print("Command выход(main.py) error", message)       


@dp.message(F.text.lower() == "=конспекты=")
async def conspekti(message: types.Message):
    try:
        await COMMANDS_cmd_conspekti.cmd_conspekti(message)
    except:
        print("Command =Конспекты=(main.py) error", message)


@dp.message(F.text.lower() == "цимпа")
async def CIMPY_selected(message: types.Message):
    try:
        await COMMANDS_cmd_conspekti.CIMPY_selected(message)
    except:
        print("Command цимпа(main.py) error", message)       


@dp.callback_query(F.data[:6] == "CIMPY-")
async def send_random_value(callback: types.CallbackQuery):
    #try:
        number = str(callback.data)[6:]
        document = FSInputFile('assets/cimpy/LR'+number+'.pdf')
        await bot.send_document(chat_id = callback.from_user.id, document= document, caption="Ваша лабораторная работа №"+number+"!")
        await callback.answer(
            text="Спасибо, что воспользовались ботом! " + number,
            show_alert=True)
    #except:
        #print("CALLBACK_QUERY 'CIMPY-' (main.py) error", callback)



async def main():
     await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())