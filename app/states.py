from aiogram.fsm.state import State, StatesGroup


class AddTaskState(StatesGroup):
    task = State()
    