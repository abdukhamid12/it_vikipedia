import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command
from btn import *
from avto import *

BOT_TOKEN = "6600379465:AAEf5a5cCTMtJ3HSj1L8Msd94UdK-w1fEoY"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)


async def command_menu(dispa: Dispatcher):
  await dispa.bot.set_my_commands(
    [
      types.BotCommand('start', 'Ishga tushirish'),
    ]
  )

@dp.message_handler(commands=['start'])
async def get_start(message:types.Message):
    await message.answer(f"Salom {message.from_user.first_name}", reply_markup=menu)

@dp.message_handler(text='🏍 Motosikl')
async def get_moto(message:types.Message):
  await message.answer("Motosikl turini tanlang: ", reply_markup=moto_menu)

@dp.message_handler(text='🚘 Yengil moshinalar')
async def get_auto(message:types.Message):
  await message.answer("Yengil moshinalar turini tanlang: ", reply_markup=yengil_auto_menu)

@dp.message_handler(text="🚛 Og'ir moshinalar")
async def get_ogir(message:types.Message):
  await message.answer("Og'ir moshinalar turini tanlang: ", reply_markup=ogir_auto_menu)

@dp.message_handler(text="Klassik")
async def get_klassik(message:types.Message):
  img = klassik['img']
  context = f"Nomi: {klassik['name']}\nNarxi: {klassik['price']}\nMalumot: {klassik['malumot']}"

  await message.answer_photo(img, caption=context)

@dp.message_handler(text="Motard")
async def get_motard(message:types.Message):
  img1 = motard['img']
  context1 = f"Nomi: {motard['name']}\nNarxi: {motard['price']}\nMalumot: {motard['malumot']}"

  await message.answer_photo(img1, caption=context1)

@dp.message_handler(text="Dregster")
async def get_dregster(message:types.Message):
  img2 = dregster['img']
  context2 = f"Nomi: {dregster['name']}\nNarxi: {dregster['price']}\nMalumot: {dregster['malumot']}"

  await message.answer_photo(img2, caption=context2)

@dp.message_handler(text="BMW X7")
async def get_x7(message:types.Message):
  img3 = bmw_x7['img']
  context3 = f"Nomi: {bmw_x7['name']}\nNarxi: {bmw_x7['price']}\nMalumot: {bmw_x7['malumot']}"

  await message.answer_photo(img3, caption=context3)

@dp.message_handler(text="Equinox")
async def get_equinox(message:types.Message):
  img4 = equinox['img']
  context4 = f"Nomi: {equinox['name']}\nNarxi: {equinox['price']}\nMalumot: {equinox['malumot']}"

  await message.answer_photo(img4, caption=context4)


@dp.message_handler(text="Tracker 1")
async def get_tracker(message: types.Message):
  img5 = tracker['img']
  context5 = f"Nomi: {tracker['name']}\nNarxi: {tracker['price']}\nMalumot: {tracker['malumot']}"

  await message.answer_photo(img5, caption=context5)

@dp.message_handler(text='🔙 orqaga')
async def get_back_menu(message: types.Message):
  await get_start(message)


if __name__ == "__main__":
  executor.start_polling(dp, on_startup=command_menu)