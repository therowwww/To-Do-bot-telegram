from aiogram import Router, types
from aiogram.filters import Command
from task import tasks


router = Router()


@router.message(Command('list'))
async def list_tasks(message: types.Message):
    if not tasks:
        await message.answer("Task list is empty.")
        return

    task_list = "\n".join([f"{key}: {value}" for key, value in tasks.items()])
    await message.answer(f"Your task list:\n{task_list}")