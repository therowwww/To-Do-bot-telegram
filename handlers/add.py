from aiogram.fsm.context import FSMContext
from aiogram import Router, types
from aiogram.filters import Command
from task import TaskStates, tasks


router = Router()


@router.message(Command("add"))
async def add_task(message: types.Message, state: FSMContext):
    await message.answer("Enter a task to add to the list:")

    await state.set_state(TaskStates.add)

@router.message(TaskStates.add)
async def process_task_input(message: types.Message, state: FSMContext):
    task_text = message.text

    if not task_text:
        await message.answer("Please enter a valid task.")
        return

    tasks[str(len(tasks) + 1)] = task_text

    await message.answer(f"Task added successfully!")
    await state.clear()
