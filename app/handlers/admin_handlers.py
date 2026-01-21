from aiogram import Router, F, types
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from config.config_reader import ADMINS
from app.database.database import payments_save_user
from app.database.database import payments_orders

router_admin = Router()

def is_admin(user_id: int)-> bool:
    return user_id in ADMINS


@router_admin.message(Command("paid"))
async def admin_panel(message: types.Message):
    if not is_admin(message.from_user.id):
        await message.answer("Извините данная команда доступна только для пользователей")
        return
    total = payments_orders()
    await message.answer(f"Всего пользователей {total}")

