from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_contact_keyboard():
    raw_keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Kontaktni yuborish", 
                        request_contact=True,
                        )]
    ], resize_keyboard=True, input_field_placeholder='+998', one_time_keyboard=True)

    return raw_keyboard

