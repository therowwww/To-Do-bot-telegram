from aiogram import Router, types
from aiogram.filters import Command
from task import tasks

router = Router()


@router.message(Command("clear"))
async def verify_clear(message: types.Message):
    await message.answer("Are you sure you want to delete all tasks?\n/delete - Delete all tasks\n/no - Cancel")


@router.message(Command("no"))
async def cancel_clear(message: types.Message):
    await message.answer("Action cancelled!")

@router.message(Command("delete"))
async def clear_tasks(message: types.Message):
    tasks.clear()
    await message.answer("All tasks have been deleted.")