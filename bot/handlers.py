from .dispatcher import dispatcher

from aiogram.filters import Command
from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from models.models import UserData
from .states import MainStates
from .keyboards import get_contact_keyboard

@dispatcher.message(Command(commands=['start']))
async def startCommandHandler( message : Message,bot : Bot, state: FSMContext):
    await state.clear()
    await state.set_state(MainStates.GET_CONTACT)
    await message.answer('Iltimos, kontaktingizni yuboring', reply_markup=get_contact_keyboard())
    return 


@dispatcher.message(MainStates.GET_CONTACT)
async def getContactHandler( message : Message,bot : Bot, state : FSMContext):
    if not message.contact:
        await message.answer('Faqat kontakt qabul qilinadi.')
        return 
    if message.contact.user_id != message.from_user.id:
        await message.answer('Faqat ozingizni kontaktingizni yubora olasiz.')
        return 
    number = message.contact.phone_number
    userdata, created  = UserData.objects.get_or_create(phone=number)
    userdata.telegram_id = message.from_user.id
    userdata.save()
    await message.answer(f'Sizning kontaktingiz ({number}) qabul qilindi')
    await state.clear()

