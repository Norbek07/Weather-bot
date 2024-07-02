from loader import dp, bot
from aiogram import F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from states.havo_stt import ObHavo
from aiogram import types
from weather import get_weather
from keyboard_buttons.weather_button import havo_button
from keyboard_buttons.weather_inl_b import weather_inl_button

@dp.message(F.text=="Weather ⛅️")
async def get_weather_command(message: Message,state:FSMContext):
    await message.answer(text="Shaharni tanlang !", reply_markup=weather_inl_button) # reply_markup=havo_button, 
    await state.set_state(ObHavo.havo)

# @dp.message(ObHavo.havo)
# async def send_weather(message: Message, state:FSMContext):
#     city = message.text
#     weather = get_weather(city) 
    
#     Vaqt = weather.get("Vaqt", "Noma'lum")
#     Harorat = weather.get("Harorat", "Noma'lum")
#     Bosim = weather.get("Bosim", "Noma'lum")
#     Namlik = weather.get("Namlik", "Noma'lum")
#     Shamol = weather.get("Shamol", "Noma'lum")

#     javob = (f"⛅️ 𝗢𝗯-𝗵𝗮𝘃𝗼 𝗺𝗮'𝗹𝘂𝗺𝗼𝘁𝗹𝗮𝗿𝗶:\n\n⏰ Vaqt : {Vaqt}\n\n🌡 Harorat : {Harorat}\n\n🌬 Bosim : {Bosim}\n\n💧 Namlik : {Namlik}\n\n💨 Shamol: {Shamol}")
#     await message.answer(javob)
# 𝑶𝒃-𝒉𝒂𝒗𝒐 𝒎𝒂'𝒍𝒖𝒎𝒐𝒕𝒍𝒂𝒓𝒊

# ташкент Toshkent
@dp.callback_query(F.data=="ташкент", ObHavo.havo)
async def Toshkent(callback:CallbackQuery):
    await callback.answer("Toshkent")

    city = callback.message.text
    weather = get_weather("ташкент")

    Vaqt = weather.get("Vaqt", "Noma'lum")
    Harorat = weather.get("Harorat", "Noma'lum")
    Bosim = weather.get("Bosim", "Noma'lum")
    Namlik = weather.get("Namlik", "Noma'lum")
    Shamol = weather.get("Shamol", "Noma'lum")

    javob = (f"⛅️ 𝗢𝗯-𝗵𝗮𝘃𝗼 𝗺𝗮'𝗹𝘂𝗺𝗼𝘁𝗹𝗮𝗿𝗶: Toshkent\n\n⏰ Vaqt : {Vaqt}\n\n🌡 Harorat : {Harorat}\n\n🌬 Bosim : {Bosim}\n\n💧 Namlik : {Namlik}\n\n💨 Shamol: {Shamol}")
    
    await callback.message.answer(text=javob,reply_markup=weather_inl_button)
    await callback.message.delete()

# бухара Buxoro
@dp.callback_query(F.data=="бухара", ObHavo.havo)
async def Buxoro(callback:CallbackQuery):
    await callback.answer("Buxoro")

    city = callback.message.text
    weather = get_weather("бухара")
    
    Vaqt = weather.get("Vaqt", "Noma'lum")
    Harorat = weather.get("Harorat", "Noma'lum")
    Bosim = weather.get("Bosim", "Noma'lum")
    Namlik = weather.get("Namlik", "Noma'lum")
    Shamol = weather.get("Shamol", "Noma'lum")

    javob = (f"⛅️ 𝗢𝗯-𝗵𝗮𝘃𝗼 𝗺𝗮'𝗹𝘂𝗺𝗼𝘁𝗹𝗮𝗿𝗶: Buxoro\n\n⏰ Vaqt : {Vaqt}\n\n🌡 Harorat : {Harorat}\n\n🌬 Bosim : {Bosim}\n\n💧 Namlik : {Namlik}\n\n💨 Shamol: {Shamol}")
    
    await callback.message.answer(text=javob,reply_markup=weather_inl_button)
    await callback.message.delete()
# навои Navoiy
@dp.callback_query(F.data=="навои", ObHavo.havo)
async def Navoiy(callback:CallbackQuery):
    await callback.answer("Navoiy")

    city = callback.message.text
    weather = get_weather("навои")
    
    Vaqt = weather.get("Vaqt", "Noma'lum")
    Harorat = weather.get("Harorat", "Noma'lum")
    Bosim = weather.get("Bosim", "Noma'lum")
    Namlik = weather.get("Namlik", "Noma'lum")
    Shamol = weather.get("Shamol", "Noma'lum")

    javob = (f"⛅️ 𝗢𝗯-𝗵𝗮𝘃𝗼 𝗺𝗮'𝗹𝘂𝗺𝗼𝘁𝗹𝗮𝗿𝗶: Navoiy\n\n⏰ Vaqt : {Vaqt}\n\n🌡 Harorat : {Harorat}\n\n🌬 Bosim : {Bosim}\n\n💧 Namlik : {Namlik}\n\n💨 Shamol: {Shamol}")
    
    await callback.message.answer(text=javob,reply_markup=weather_inl_button)
    await callback.message.delete()

# сырдарья Sirdaryo
@dp.callback_query(F.data=="сырдарья", ObHavo.havo)
async def Sirdaryo(callback:CallbackQuery):
    await callback.answer("Sirdaryo")

    city = callback.message.text
    weather = get_weather("сырдарья")
    
    Vaqt = weather.get("Vaqt", "Noma'lum")
    Harorat = weather.get("Harorat", "Noma'lum")
    Bosim = weather.get("Bosim", "Noma'lum")
    Namlik = weather.get("Namlik", "Noma'lum")
    Shamol = weather.get("Shamol", "Noma'lum")

    javob = (f"⛅️ 𝗢𝗯-𝗵𝗮𝘃𝗼 𝗺𝗮'𝗹𝘂𝗺𝗼𝘁𝗹𝗮𝗿𝗶: Sirdaryo\n\n⏰ Vaqt : {Vaqt}\n\n🌡 Harorat : {Harorat}\n\n🌬 Bosim : {Bosim}\n\n💧 Namlik : {Namlik}\n\n💨 Shamol: {Shamol}")
    
    await callback.message.answer(text=javob,reply_markup=weather_inl_button)
    await callback.message.delete()

# самарканд Samarqand
@dp.callback_query(F.data=="самарканд", ObHavo.havo)
async def Samarqand(callback:CallbackQuery):
    await callback.answer("Samarqand")

    city = callback.message.text
    weather = get_weather("самарканд")
    
    Vaqt = weather.get("Vaqt", "Noma'lum")
    Harorat = weather.get("Harorat", "Noma'lum")
    Bosim = weather.get("Bosim", "Noma'lum")
    Namlik = weather.get("Namlik", "Noma'lum")
    Shamol = weather.get("Shamol", "Noma'lum")

    javob = (f"⛅️ 𝗢𝗯-𝗵𝗮𝘃𝗼 𝗺𝗮'𝗹𝘂𝗺𝗼𝘁𝗹𝗮𝗿𝗶: Samarqand\n\n⏰ Vaqt : {Vaqt}\n\n🌡 Harorat : {Harorat}\n\n🌬 Bosim : {Bosim}\n\n💧 Namlik : {Namlik}\n\n💨 Shamol: {Shamol}")
    
    await callback.message.answer(text=javob,reply_markup=weather_inl_button)
    await callback.message.delete()

# фергана Fargona
@dp.callback_query(F.data=="фергана", ObHavo.havo)
async def Fargona(callback:CallbackQuery):
    await callback.answer("Farg'ona")

    city = callback.message.text
    weather = get_weather("фергана")
    
    Vaqt = weather.get("Vaqt", "Noma'lum")
    Harorat = weather.get("Harorat", "Noma'lum")
    Bosim = weather.get("Bosim", "Noma'lum")
    Namlik = weather.get("Namlik", "Noma'lum")
    Shamol = weather.get("Shamol", "Noma'lum")

    javob = (f"⛅️ 𝗢𝗯-𝗵𝗮𝘃𝗼 𝗺𝗮'𝗹𝘂𝗺𝗼𝘁𝗹𝗮𝗿𝗶: Farg'ona\n\n⏰ Vaqt : {Vaqt}\n\n🌡 Harorat : {Harorat}\n\n🌬 Bosim : {Bosim}\n\n💧 Namlik : {Namlik}\n\n💨 Shamol: {Shamol}")
    
    await callback.message.answer(text=javob,reply_markup=weather_inl_button)
    await callback.message.delete()

# наманган Namangan
@dp.callback_query(F.data=="наманган", ObHavo.havo)
async def Namangan(callback:CallbackQuery):
    await callback.answer("Namangan")

    city = callback.message.text
    weather = get_weather("наманган")
    
    Vaqt = weather.get("Vaqt", "Noma'lum")
    Harorat = weather.get("Harorat", "Noma'lum")
    Bosim = weather.get("Bosim", "Noma'lum")
    Namlik = weather.get("Namlik", "Noma'lum")
    Shamol = weather.get("Shamol", "Noma'lum")

    javob = (f"⛅️ 𝗢𝗯-𝗵𝗮𝘃𝗼 𝗺𝗮'𝗹𝘂𝗺𝗼𝘁𝗹𝗮𝗿𝗶: Namangan\n\n⏰ Vaqt : {Vaqt}\n\n🌡 Harorat : {Harorat}\n\n🌬 Bosim : {Bosim}\n\n💧 Namlik : {Namlik}\n\n💨 Shamol: {Shamol}")
    
    await callback.message.answer(text=javob,reply_markup=weather_inl_button)
    await callback.message.delete()

# андижан Andijon
@dp.callback_query(F.data=="андижан", ObHavo.havo)
async def Andijon(callback:CallbackQuery):
    await callback.answer("Andijon")

    city = callback.message.text
    weather = get_weather("андижан")
    
    Vaqt = weather.get("Vaqt", "Noma'lum")
    Harorat = weather.get("Harorat", "Noma'lum")
    Bosim = weather.get("Bosim", "Noma'lum")
    Namlik = weather.get("Namlik", "Noma'lum")
    Shamol = weather.get("Shamol", "Noma'lum")

    javob = (f"⛅️ 𝗢𝗯-𝗵𝗮𝘃𝗼 𝗺𝗮'𝗹𝘂𝗺𝗼𝘁𝗹𝗮𝗿𝗶: Andijon\n\n⏰ Vaqt : {Vaqt}\n\n🌡 Harorat : {Harorat}\n\n🌬 Bosim : {Bosim}\n\n💧 Namlik : {Namlik}\n\n💨 Shamol: {Shamol}")
    
    await callback.message.answer(text=javob,reply_markup=weather_inl_button)
    await callback.message.delete()

# джизак Jizzah
@dp.callback_query(F.data=="джизак", ObHavo.havo)
async def Jizzah(callback:CallbackQuery):
    await callback.answer("Jizzah")

    city = callback.message.text
    weather = get_weather("джизак")
    
    Vaqt = weather.get("Vaqt", "Noma'lum")
    Harorat = weather.get("Harorat", "Noma'lum")
    Bosim = weather.get("Bosim", "Noma'lum")
    Namlik = weather.get("Namlik", "Noma'lum")
    Shamol = weather.get("Shamol", "Noma'lum")

    javob = (f"⛅️ 𝗢𝗯-𝗵𝗮𝘃𝗼 𝗺𝗮'𝗹𝘂𝗺𝗼𝘁𝗹𝗮𝗿𝗶: Jizzah\n\n⏰ Vaqt : {Vaqt}\n\n🌡 Harorat : {Harorat}\n\n🌬 Bosim : {Bosim}\n\n💧 Namlik : {Namlik}\n\n💨 Shamol: {Shamol}")
    
    await callback.message.answer(text=javob,reply_markup=weather_inl_button)
    await callback.message.delete()

# ургенч Urganch
@dp.callback_query(F.data=="ургенч", ObHavo.havo)
async def Urganch(callback:CallbackQuery):
    await callback.answer("Urganch")

    city = callback.message.text
    weather = get_weather("ургенч")
    
    Vaqt = weather.get("Vaqt", "Noma'lum")
    Harorat = weather.get("Harorat", "Noma'lum")
    Bosim = weather.get("Bosim", "Noma'lum")
    Namlik = weather.get("Namlik", "Noma'lum")
    Shamol = weather.get("Shamol", "Noma'lum")

    javob = (f"⛅️ 𝗢𝗯-𝗵𝗮𝘃𝗼 𝗺𝗮'𝗹𝘂𝗺𝗼𝘁𝗹𝗮𝗿𝗶: Urganch\n\n⏰ Vaqt : {Vaqt}\n\n🌡 Harorat : {Harorat}\n\n🌬 Bosim : {Bosim}\n\n💧 Namlik : {Namlik}\n\n💨 Shamol: {Shamol}")
    
    await callback.message.answer(text=javob,reply_markup=weather_inl_button)
    await callback.message.delete()

# нукус Nukus
@dp.callback_query(F.data=="нукус", ObHavo.havo)
async def Nukus(callback:CallbackQuery):
    await callback.answer("Nukus")

    city = callback.message.text
    weather = get_weather("нукус")
    
    Vaqt = weather.get("Vaqt", "Noma'lum")
    Harorat = weather.get("Harorat", "Noma'lum")
    Bosim = weather.get("Bosim", "Noma'lum")
    Namlik = weather.get("Namlik", "Noma'lum")
    Shamol = weather.get("Shamol", "Noma'lum")

    javob = (f"⛅️ 𝗢𝗯-𝗵𝗮𝘃𝗼 𝗺𝗮'𝗹𝘂𝗺𝗼𝘁𝗹𝗮𝗿𝗶: Nukus\n\n⏰ Vaqt : {Vaqt}\n\n🌡 Harorat : {Harorat}\n\n🌬 Bosim : {Bosim}\n\n💧 Namlik : {Namlik}\n\n💨 Shamol: {Shamol}")
    
    await callback.message.answer(text=javob,reply_markup=weather_inl_button)
    await callback.message.delete()

# термез Termiz
@dp.callback_query(F.data=="термез", ObHavo.havo)
async def Termiz(callback:CallbackQuery):
    await callback.answer("Termiz")

    city = callback.message.text
    weather = get_weather("термез")
    
    Vaqt = weather.get("Vaqt", "Noma'lum")
    Harorat = weather.get("Harorat", "Noma'lum")
    Bosim = weather.get("Bosim", "Noma'lum")
    Namlik = weather.get("Namlik", "Noma'lum")
    Shamol = weather.get("Shamol", "Noma'lum")

    javob = (f"⛅️ 𝗢𝗯-𝗵𝗮𝘃𝗼 𝗺𝗮'𝗹𝘂𝗺𝗼𝘁𝗹𝗮𝗿𝗶: Termiz\n\n⏰ Vaqt : {Vaqt}\n\n🌡 Harorat : {Harorat}\n\n🌬 Bosim : {Bosim}\n\n💧 Namlik : {Namlik}\n\n💨 Shamol: {Shamol}")
    
    await callback.message.answer(text=javob,reply_markup=weather_inl_button)
    await callback.message.delete()
