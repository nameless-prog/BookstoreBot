from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message
from .keyboards import main_keyboard

router = Router()

@router.message(Command(commands=["start"]))
async def cmd_start(message: Message):
    await message.answer(
        f"Привет {message.from_user.full_name}, я магазин твоих любимых книг\n"
        f"Прошу, нажми на кнопку:",
        reply_markup=main_keyboard()
    )

@router.callback_query()
async def main_buttons(callback: types.CallbackQuery):
    if callback.data == "catalog":
        await callback.message.answer("📖 Вот каталог книг:", callback = "choose_catalog")
    
    elif callback.data == "about":
        await callback.message.answer("Этот чат-бот: магазин книг")

    elif callback.data == "close":
        await callback.message.edit_text("Меню закрыто ❌")


    await callback.answer()

