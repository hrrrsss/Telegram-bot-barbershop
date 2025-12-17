from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def start_kb(flag: str) -> ReplyKeyboardBuilder:
    kb_builder = ReplyKeyboardBuilder()
    if flag == "exist":
        kb_builder.row(KeyboardButton(text="Выбрать барбера"),
                       KeyboardButton(text="Отмена брони"))
    else:
        kb_builder.row(KeyboardButton(text="Выбрать барбера"))
    return kb_builder.as_markup(resize_keyboard=True)


def barbers_kb(barbers: None | list) -> ReplyKeyboardBuilder:
    kb_builder = ReplyKeyboardBuilder()
    if barbers:
        buttons = [KeyboardButton(text='✂️'+barber) for barber in barbers]
        kb_builder.row(*buttons)
    kb_builder.row(KeyboardButton(text="👈На главную"))
    return kb_builder.as_markup(resize_keyboard=True)
