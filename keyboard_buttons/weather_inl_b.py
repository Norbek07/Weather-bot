from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
weather_inl_button = InlineKeyboardMarkup(
    inline_keyboard=[
[InlineKeyboardButton(text="Toshkent", callback_data="ташкент"), InlineKeyboardButton(text="Buxoro", callback_data="бухара")],
[InlineKeyboardButton(text="Navoiy", callback_data="навои"), InlineKeyboardButton(text="Sirdaryo", callback_data="сырдарья")],
[InlineKeyboardButton(text="Samarqand", callback_data="самарканд"), InlineKeyboardButton(text="Farg'ona", callback_data="фергана")],
[InlineKeyboardButton(text="Namangan", callback_data="наманган"), InlineKeyboardButton(text="Andijon", callback_data="андижан")],
[InlineKeyboardButton(text="Jizzah", callback_data="джизак"), InlineKeyboardButton(text="Urganch", callback_data="ургенч")],
[InlineKeyboardButton(text="Nukus", callback_data="нукус"), InlineKeyboardButton(text="Termiz", callback_data="термез")],
    ]
)