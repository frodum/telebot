from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types
from tok import TOKEN
from tok import Player
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.types import Message
import random
from keyboards import *

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=tok.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
pravila = InlineKeyboardButton("How play", url="https://moscow.questoria.ru/game-mafia")
play = InlineKeyboardButton("PLAY", callback_data='play')
btns1 = InlineKeyboardMarkup().add(pravila, play)

btns2 = InlineKeyboardMarkup
a = []


@dp.message_handler(commands=["start"], state="wlkm")
async def welkome(message: types.Message, state: FSMContext):
    await message.reply(
        "Hi I'm game bot. Now You can play mafia. Press on button 'How play', if you don't know how play in  mafia.",
        reply_markup=btns)


@dp.callback_query_handler(func=lambda c: c.data and c.data.startswith('play'))
async def wait(message: types.Message):
    cards = ['mafia', 'mir', 'mir', 'cami', 'dok']
    a.append(message.from_user.id)
    await message.reply("Game start")
    player = Player(message.from_user.id, message.from_user.username, random.choice(cards))
    cards.extend(player.rol)
    print(cards, player.rol)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
