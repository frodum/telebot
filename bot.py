from aiogram import Bot, Dispatcher, executor, types
import logging
from tok import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import random

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

shooters = KeyboardButton("/shooters")
arcades = KeyboardButton("/arcades")
sborniky = KeyboardButton("/imulators")
CG=KeyboardButton("/i cant find game for me")
cryi=InlineKeyboardButton("cry islands", url="https://www.crazygames.com/game/cry-islands")
cs = InlineKeyboardButton("cs 1.6", url="https://play-cs.com/ru/servers")
krunker = InlineKeyboardButton("krunker.io", url="https://krunker.io/")
venge = InlineKeyboardButton("venge.io", url="https://venge.io/")
warblokes = InlineKeyboardButton("WarBlokes", url="https://warbrokers.io/signin.php")
agar = InlineKeyboardButton("agar io", url="https://agario-game.ru/")
slither = InlineKeyboardButton("slither io", url="https://slither.io/")
diep = InlineKeyboardButton("diep io", url="https://diep.io/")
mario = InlineKeyboardButton("Mario(+)", url="https://supermario-game.com/ru")
ok = InlineKeyboardButton("OK(there every old games!)", url="https://okgamer.ru/")
butshoot = InlineKeyboardMarkup().add(cs, krunker, venge, cryi)
buts1 = ReplyKeyboardMarkup().add(shooters, sborniky, arcades, CG)
butarcade = InlineKeyboardMarkup().add(agar, slither, diep)
butimul = InlineKeyboardMarkup().add(ok, mario)
craz=InlineKeyboardButton("crazy games", url="https://www.crazygames.com/")
cras=InlineKeyboardMarkup().add(craz)

@dp.message_handler(commands=['start'], state='*')
async def _(message: types.Message, state: FSMContext):
    await message.reply("Hi, \nI,m Bot who can help you with finding web games.")
    await message.reply("choose janr", reply_markup=buts1)


@dp.message_handler(commands="shooters")
async def shoot(message: types.Message):
    await message.reply("Shooters \nYou can play in:", reply_markup=butshoot)


@dp.message_handler(commands="arcades")
async def shoot(message: types.Message):
    await message.reply("Arcades \nYou can play in:", reply_markup=butarcade)

@dp.message_handler(commands="imulators")
async def shoot(message: types.Message):
    await message.reply("Imulators \nYou can play in:", reply_markup=butimul)

@dp.message_handler(commands="/i cant find game for me")
async def shoot(message: types.Message):
    await message.reply("If you cant find games for you \nYou can go in:", reply_markup=cras)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
