from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .routers import router

def main_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📚 Каталог", callback_data="catalog")
            ],
            [
                InlineKeyboardButton(text="ℹ️ О нас", callback_data="about")
            ],
            [
                InlineKeyboardButton(text="❌ Закрыть", callback_data="close")
            ]
        ]
    )
    return keyboard