from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from data_views import (get_user_id, get_appointments)
from data_exchanger import create_user
from lexicon import lexicon_user
from keyboards.user_kb import start_kb


start_router = Router()


@start_router.message((F.text == "/start") | (F.text == "👈 На главную"))
async def start_cmd(message: Message, state: FSMContext):
    await state.clear()

    user_name = message.from_user.full_name
    user_id = message.from_user.id

    db_user_id = await get_user_id(message.from_user.id)
    appoint = await get_appointments(db_user_id)

    if db_user_id:
        if appoint:
            keyboard = start_kb("exist")
        else:
            keyboard = start_kb("notexists")           
    else:
        await create_user(user_name, user_id)

    await message.answer(lexicon_user.START, 
                         reply_markup=keyboard)