from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types
import tok
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.types import Message
import random

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=tok.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
pravila = InlineKeyboardButton("How play", url="https://moscow.questoria.ru/game-mafia")
play = InlineKeyboardButton("PLAY", callback_data="play")
btns = InlineKeyboardMarkup().add(pravila, play)
a = []


@dp.message_handler(commands=["start"])
async def welkome(message: types.Message):
    await message.reply(
        "Hi I'm game bot. Now You can play mafia. Press on button if you don't know how play in  mafia.",
        reply_markup=btns)


@dp.message_handler()
async def wait(message: types.Message):
    a.append(message.from_user.id)
    btns


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
