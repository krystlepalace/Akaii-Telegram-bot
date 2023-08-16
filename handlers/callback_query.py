from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.enums.chat_member_status import ChatMemberStatus
import main
from filters import group

router = Router()

@router.callback_query()
async def process_anim_toggle_callback(callback: CallbackQuery):
    if await group.isAdmin(callback.message, callback.from_user.id):
        bot_member = await callback.message.chat.get_member(user_id=callback.message.from_user.id)
        if bot_member.status == ChatMemberStatus.ADMINISTRATOR:
            if callback.data == 'anim0':
                main.animations_allowed = True
                await callback.message.answer("Аминированные стикеры разрешены!")
                await callback.answer()
            if callback.data == 'anim1':
                main.animations_allowed = False
                await callback.message.answer("Анимированные стикеры запрещены.")
                await callback.answer()
        else:
            await callback.message.answer(
                    "Бот не является администратором."
                    )
    else:
        await callback.message.answer(
                "Вы не являетесь администратором."
                )
        await callback.answer()
