from aiogram.fsm.state import State, StatesGroup


class CreateAppointment(StatesGroup):
    barber = State()
    service = State()
    date = State()
    interval_time = State()
    time = State()