import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = "8481770525:AAFImlsm6riC9r6dHGB2a3U4l5Eb-QCn3Qk"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())