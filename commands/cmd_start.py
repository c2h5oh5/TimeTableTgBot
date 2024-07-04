from aiogram.types import WebAppInfo
from aiogram import *
import aiogram.types as types
from aiogram.utils.keyboard import InlineKeyboardBuilder


main_kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Расписание", web_app=WebAppInfo(url='https://spiral-able-bagpipe.glitch.me/'))],
            [types.KeyboardButton(text="=Конспекты=")]
        ],
        resize_keyboard=True,
        input_field_placeholder="Главная"
    )


async def cmd_start(message: types.Message):
    await message.answer("Привет!!!", reply_markup=main_kb, reply_to_message_id=message.message_id)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
            text= str("WebApp"),
            web_app = WebAppInfo(url='https://spiral-able-bagpipe.glitch.me/'),
            callback_data= "WedApp-Opened"))
    await message.answer("Заходи", reply_markup = builder.as_markup())
    
   
async def cmd_exit(message: types.Message):
    await message.answer("Вы вышли в главное меню", reply_markup=main_kb, reply_to_message_id=message.message_id)