from aiogram import Router, F
from aiogram.types import Message , InlineKeyboardButton , InlineKeyboardMarkup , CallbackQuery
from aiogram.filters.command import Command
from aiogram.filters import CommandObject , Text 
from aiogram.utils.keyboard import InlineKeyboardBuilder 
from aiogram.fsm.state import StatesGroup , State 
from aiogram.fsm.context import FSMContext
from aiogram.types import BotCommand , BotCommandScope , BotCommandScopeAllGroupChats
from aiogram.enums import ContentType , ChatType 

router = Router()

ADMIN_GROUP = None

admin_chat = F.chat.id == ADMIN_GROUP

@router.message(Command('admin'), admin_chat)
async def router_message_answer(message:Message):
    await message.answer('admin_message')