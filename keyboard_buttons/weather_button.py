from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


obh_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Weather ⛅️")]
        
    ],
   resize_keyboard=True,
   input_field_placeholder="Menudan birini tanlang"
)

havo_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ташкент"),KeyboardButton(text="бухара"),],
        [KeyboardButton(text="навои"),KeyboardButton(text="сырдарья"),],
        [KeyboardButton(text="самарканд"),KeyboardButton(text="фергана"),],
        [KeyboardButton(text="наманган"),KeyboardButton(text="андижан"),],
        [KeyboardButton(text="джизак"),KeyboardButton(text="ургенч"),],
        [KeyboardButton(text="нукус"),KeyboardButton(text="термез"),],
        
    ],
   resize_keyboard=True,
   input_field_placeholder="Menudan birini tanlang"
)






