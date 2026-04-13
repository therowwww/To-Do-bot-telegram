from aiogram import Router, types
from task import tasks
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class RemoveTask(StatesGroup):
    waiting_for_task_id = State()


router = Router()


@router.message(Command('remove'))
async def remove_task(message: types.Message, state: FSMContext):
    if not tasks:
        await message.answer("Task list is empty.")
        return
    
    task_list = "\n".join([f"{key}: {value}" for key, value in tasks.items()])
    await message.answer(f"Your tasks:\n{task_list}\n\nEnter the task number to delete:")
    await state.set_state(RemoveTask.waiting_for_task_id)

@router.message(RemoveTask.waiting_for_task_id)
async def remove_tasks(message: types.Message, state: FSMContext):
    task_id = message.text
    if task_id in tasks:
        del tasks[task_id]
        await message.answer(f"Task successfully deleted!")
    else:
        await message.answer("Invalid task number.")
        await message.answer(f"{task_id}")
    await state.clear()