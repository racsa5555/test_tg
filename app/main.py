import asyncio

from decouple import config

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram import types
from aiogram.fsm.context import FSMContext

from dao import create_task,get_tasks
from states import AddTaskState
from utils import pretty_tasks


TOKEN = config('TOKEN')

bot = Bot(TOKEN)

dp = Dispatcher()

@dp.message(Command(commands=['start']))
async def start(message:types.Message):
    await message.answer(text = 'Привет\nВведи /add для добавления задачи или /tsk для просмотра всех задач')

@dp.message(Command(commands=['add']))
async def start_add_task(message:types.Message,state:FSMContext):
    await message.answer(text = 'Введите задачу')
    await state.set_state(AddTaskState.task)


@dp.message(AddTaskState.task)
async def add_task(message:types.Message,state:FSMContext):
    text = message.text
    res = create_task(text)
    if res:
        await message.answer(text = 'Ваша задача успешно добавлена')
        await state.set_state()
    else:
        await message.answer(text = 'Что то произошло не так, попробуйте еще раз)')
        await state.set_state()

@dp.message(Command(commands=['tsk']))
async def show_tasks(message:types.Message):
    tasks = get_tasks()
    if tasks:
        res = pretty_tasks(tasks)
        await message.answer(text = res)
    else:
        await message.answer(text = 'Задач пока что нет')


         







async def main():
    await dp.start_polling(bot)

asyncio.run(main())