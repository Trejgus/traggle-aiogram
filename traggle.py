import os, sys
import shutil

from aiogram import Dispatcher, Bot
import asyncio, logging

def copy_folder(src, dst):
    # Создаем папку назначения, если она не существует
    if not os.path.exists(dst):
        os.makedirs(dst)

    # Копируем файлы из исходной папки в папку назначения
    files = os.listdir(src)
    for file_name in files:
        file_path = os.path.join(src, file_name)
        dst_path = os.path.join(dst, file_name)
        if os.path.isfile(file_path):
            shutil.copy2(file_path, dst_path)
        elif os.path.isdir(file_path):
            copy_folder(file_path, dst_path)

    
def create_traggle_project(name_project = 'traggle-1.0.0'):
    path = os.path.abspath(__file__)[:-10]
    copy_folder(f'{path}traggle_start_folder', f'{os.getcwd()}/{name_project}')
    
def create_app(name_app = 'traggle_app_1.0.0'):
    path = os.path.abspath(__file__)[:-10]
    copy_folder(f'{path}/apps/home', f'{os.getcwd()}/{name_app}')
    
def create_email_app(name_app = 'email'):
    path = os.path.abspath(__file__)[:-10]
    copy_folder(f'{path}/apps/email', f'{os.getcwd()}/{name_app}')
    
    
class Traggle:
    
    def __init__(self, dispatcher: Dispatcher, bot: Bot):
        self.dp = dispatcher
        self.bot = bot
        self.log = True
        
    def includes(self):
        self.dp.include_routers(*self.routers)
        
    def start_message(self, message = None):
        if message:
            print(message)
        
        else: print('The project has been launched')
        
    def shutdown_message(self, message = None):
        if message:
            print(message)
        
        else: print('The project has been completed')
        
    async def start(self):
        self.includes()
        self.dp.startup.register(self.start_message)
        self.dp.shutdown.register(self.shutdown_message)
        await self.dp.start_polling(self.bot)
        
    def __call__(self, *args, **kwargs):
        if self.log:
            logging.basicConfig(level = logging.DEBUG ,
                        filename = 'log.log' ,
                        filemode = 'w',
                        format = '%(asctime)s %(levelname)s %(message)s')
            
        asyncio.run(self.start())