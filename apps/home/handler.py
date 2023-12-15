from aiogram import Router
from aiogram.types import Message , InlineKeyboardButton , InlineKeyboardMarkup , CallbackQuery
from aiogram.filters.command import Command
from aiogram.filters import CommandObject , Text 
from aiogram.utils.keyboard import InlineKeyboardBuilder 
from aiogram.fsm.state import StatesGroup , State 
from aiogram.fsm.context import FSMContext
from aiogram.types import BotCommand , BotCommandScope , BotCommandScopeAllGroupChats
from aiogram.enums import ContentType , ChatType 

from . import keyboard, tools

router = Router()

@router.message(Command('router'))
async def router_message_answer(message:Message):
    await message.answer('router message',
                         reply_markup = keyboard.first_reply_keyboard.as_markup())
    

@router.message(Command('inline'))
async def inline_keyboard(message: Message):
    await message.answer('inline keyboard',
                         reply_markup = keyboard.first_inline_keyboard.as_markup())