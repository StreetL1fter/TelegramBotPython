
from aiogram import Bot, Dispatcher 
from aiogram.enums import ParseMode
from aiogram.client.session.aiohttp import AiohttpSession

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import FSInputFile
from aiogram.enums.dice_emoji import DiceEmoji
from config.config_reader import config
import logging
import asyncio
from app.handlers.handlers import router
from app.handlers.admin_handlers import router_admin
from app.database.database import create_users_table
from app.database.database import payments_save_user
from config.config_reader import ADMINS

bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)
create_users_table()
payments_save_user()






async def main():
    dp.include_router(router_admin)
    dp.include_router(router)
    await dp.start_polling(bot)
    


asyncio.run(main())