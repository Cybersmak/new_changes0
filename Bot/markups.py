from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnProfile = KeyboardButton('ПРОФИЛЬ')
btnSub = KeyboardButton('Сводные показатели')
button_contact = KeyboardButton(text="Делись!", request_contact=True)
keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
keyboard.add(button_contact)
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True)
mainMenu.add(btnProfile,btnSub)