import asyncio
from aiogram import Bot, Dispatcher
from handlers import start_router, add_router, list_router, remove_router, clear_router

TOKEN = "BOT_TOKEN"

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(remove_router)
    dp.include_router(start_router)
    dp.include_router(add_router)
    dp.include_router(clear_router)
    dp.include_router(list_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main()) 
