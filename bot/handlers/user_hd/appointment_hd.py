from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.states import CreateAppointment
from lexicon import lexicon_user
from data_views import (get_barbers, get_service)
from keyboards.user_kb import (barbers_kb, services_kb,
                               dates_kb)
from common.generate_time import create_five_days


appointment_router = Router()


@appointment_router.message(F.text == "Выбрать барбера")
async def create_appointment(message: Message, state: FSMContext):
    barbers = [barber[1] for barber in await get_barbers()]
    keyboard = barbers_kb(barbers)

    await message.answer(lexicon_user.BARBERS,
                         reply_markup=keyboard)

    await state.set_state(CreateAppointment.barber)


@appointment_router.message(CreateAppointment.barber)
async def choice_barber(message: Message, state: FSMContext):
    barber_name = message.text.split(maxsplit=1)[-1]
    barbers = await get_barbers()
    for barber in barbers:
        if barber[1] == barber_name:
            id_barber = barber[0]
    
    await state.set_data({"barber_id": id_barber})

    await message.answer(f"Хороший выбор! {barber_name} у нас хороший специалист!")

    services = await get_service(id_barber)
    keyboard = services_kb(services)
    await message.answer(f"Выберете услугу", reply_markup=keyboard)
    
    await state.set_state(CreateAppointment.service)


@appointment_router.message(CreateAppointment.service)
async def choice_service(message: Message, state: FSMContext):
    data = await state.get_data()
    id_barber = data["barber_id"]

    service_name = message.text.split(maxsplit=1)[-1]
    services = await get_service(id_barber)
    for service in services:
        if service[1] == service_name:
            id_service = service[0]

    await state.update_data({"service_id": id_service})

    dates = create_five_days()
    keyboard = dates_kb(dates)
    await message.answer("Выберите интересующую дату",
                         reply_markup=keyboard)

    await state.set_state(CreateAppointment.date)


@appointment_router.message(CreateAppointment.date)
async def choice_date(message: Message, state: FSMContext):
    ...