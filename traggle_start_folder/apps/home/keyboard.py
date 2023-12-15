from aiogram.utils.keyboard import KeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

first_reply_keyboard = KeyboardBuilder(button_type = KeyboardButton, markup = [
    [
        KeyboardButton(text = '/start')
    ]
])

first_inline_keyboard = InlineKeyboardBuilder(markup = [
    [
        InlineKeyboardButton(text = 'GitHub Traggle', url = 'https://github.com/Trejgus?tab=repositories')
    ]
])