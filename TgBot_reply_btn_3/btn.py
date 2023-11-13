from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.row('🏍 Motosikl')
menu.row('🚘 Yengil moshinalar')
menu.row("🚛 Og'ir moshinalar")

moto_menu = ReplyKeyboardMarkup(resize_keyboard=True)
moto_menu.row("Klassik")
moto_menu.row("Motard")
moto_menu.row("Dregster")
moto_menu.row("🔙 orqaga")

yengil_auto_menu = ReplyKeyboardMarkup(resize_keyboard=True)
yengil_auto_menu.row("BMW X7")
yengil_auto_menu.row("Equinox")
yengil_auto_menu.row("Tracker 1")
yengil_auto_menu.row("🔙 orqaga")

ogir_auto_menu = ReplyKeyboardMarkup(resize_keyboard=True)
ogir_auto_menu.row("Avtobus")
ogir_auto_menu.row("Fura")
ogir_auto_menu.row("Labo")
ogir_auto_menu.row("🔙 orqaga")