from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.states import CreateAppointment
from lexicon import lexicon_user
from data_views import get_barbers
from keyboards.user_kb import barbers_kb


appointment_router = Router()


@appointment_router.message(F.text == "Выбрать барбера")
async def choice_barber(message: Message, state: FSMContext):
    barbers = await get_barbers()
    keyboard = barbers_kb(barbers)

    await message.answer(lexicon_user.BARBERS,
                         reply_markup=keyboard)

    state.set_state(CreateAppointment.barber)


@appointment_router.message(CreateAppointment.barber)
async def choice_service(message: Message, state: FSMContext):
    await state.set_data({"barber": message.text[1:]})
    

    await state.set_state(CreateAppointment.date)