from aiogram import Bot, Dispatcher, executor, types
import efn
import logging

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import random

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=efn.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
a = []


@dp.message_handler(commands=['start', 'help'], state='*')
async def send_welcome(message: types.Message, state: FSMContext):
    await message.reply("Hi!\nI'm chatBot!\nPowered by aiogram.")
    await message.answer("What Yor name?")
    await state.set_state("q1")


@dp.message_handler(commands='find', state="*")
async def wr(message: types.Message, state: FSMContext):
    a.append(message.from_user.id)
    random.shuffle(a)
    if len(a) >= 2:
        for id in a:
            if id == message.from_user.id:
                continue
            else:
                break
        target = id

        a.remove(target)
        a.remove(message.from_user.id)

        target_state: FSMContext = dp.current_state(chat=target, user=target)
        target_data = await target_state.get_data()
        target_name = target_data['name']
        user_data = await state.get_data()
        user_name = user_data['name']
        await message.answer(f"Вы связаны с {target_name}")
        await bot.send_message(target, f"Вы связаны с {user_name}")
        await state.set_state("write_to_user")
        await target_state.set_state("write_to_user")
        await state.update_data({"target": target})
        await target_state.update_data({"target": message.from_user.id})
    else:
        await message.answer("Not enough users now, wait")


@dp.message_handler(state="write_to_user")
async def _(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    user_target = user_data['target']
    target_state: FSMContext = dp.current_state(chat=user_target, user=user_target)
    target_data = await target_state.get_data()
    target_name = target_data['name']
    txt = f"{target_name} : {message.text}"
    print(txt)
    await bot.send_message(chat_id=user_target, text=txt)


@dp.message_handler(state="q1")
async def name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data({"name": name})
    await message.answer("Say Your age.")
    await state.set_state("q2")


@dp.message_handler(state="q2")
async def age(message: types.Message, state: FSMContext):
    age = int(message.text)
    await state.update_data({"age": age})
    await state.set_state("eho")
    data = await state.get_data()
    await message.answer(f"{data.get('name')}({data.get('age')}) \n"
                         "Write /find to find a sobesednic")


@dp.message_handler(state="eho")
async def echo(message: types.Message, state: FSMContext):
    state_name = await state.get_state()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
