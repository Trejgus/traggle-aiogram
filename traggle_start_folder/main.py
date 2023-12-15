from aiogram import Bot , Dispatcher , html , F
from aiogram.types import Message , InlineKeyboardButton , InlineKeyboardMarkup , CallbackQuery
from aiogram.filters.command import Command
from aiogram.filters import CommandObject , Text 
from aiogram.utils.keyboard import InlineKeyboardBuilder 
from aiogram.fsm.state import StatesGroup , State 
from aiogram.fsm.context import FSMContext
from aiogram.types import BotCommand , BotCommandScope , BotCommandScopeAllGroupChats
from aiogram.enums import ContentType , ChatType  

from traggle import Traggle

import logging
import asyncio

# HANDLERS
# from handlers.start_handler import start_handler
# from handlers.admin import admin
from apps.home import handler as home
from apps.admin import handler as admin

bot = Bot('5223153520:AAEhoka4frLhOH6efQz7C68Wl5dvAtIur54')
dp = Dispatcher()




@dp.message(Command('start'))
async def start_cmd(message:Message):
    await message.answer('Hello World')
    
# <---YOUR HANDLERS--->
  
class StartBot(Traggle):
    
    routers = [home.router, admin.router] 
   
   
   
if __name__ == '__main__':
    start_bot = StartBot(dp, bot)
    start_bot()