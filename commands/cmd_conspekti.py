from aiogram import *
import aiogram.types as types
from aiogram.utils.keyboard import InlineKeyboardBuilder

kb = [
        [types.KeyboardButton(text="Цимпа"), types.KeyboardButton(text="КТСТ")],
        [types.KeyboardButton(text="Выход")]
    ]


async def cmd_conspekti(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard= kb,
        resize_keyboard= True,
    )
    await message.answer("Выберите предмет:", reply_markup=keyboard, reply_to_message_id=message.message_id)


async def CIMPY_selected(message: types.Message):
    builder = InlineKeyboardBuilder()
    for i in range(1, 21):
        builder.add(types.InlineKeyboardButton(
            text= str(i),
            callback_data= "CIMPY-"+str(i)
        ))
    builder.adjust(5)
    await message.answer("Выберите лабораторную работу:", reply_markup = builder.as_markup())


async def LABA_CIMPY(callback_message: types.message):
    await print("Callback successfull")