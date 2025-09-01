import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import routers
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, force=True)

load_dotenv()
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise RuntimeError("TOKEN not found. Put TOKEN=... into .env")

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(routers.router)

async def main():
    logging.info("🟢 Bot started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except(KeyboardInterrupt, SystemExit, SystemError):
        logging.info("🛑 Bot stopped manually")

