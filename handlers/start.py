from aiogram import Router, types
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Hi, I'm a To-Do bot!\nHere's my list of commands:\n\n1. /add - Add a task\n2. /list - Show task list\n3. /remove - Delete a task\n4. /clear - Clear all tasks")