from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ContentType
from keyboards.toggles import anim_inline
from aiogram import F
from utils.neuro.stt import STT
import os
from pathlib import Path
import main


router = Router()
stt = STT()

@router.message(Command("animations"))
async def toggle_animated_stickers(message: Message):
    await message.answer(
            "Разрешить анимированные стикеры?",
            reply_markup=anim_inline()
            )


@router.message(F.sticker)
async def check_sticker(message: Message):
    if not main.animations_allowed:
        if message.sticker and (message.sticker.is_video or message.sticker.is_animated):
            await message.delete()


@router.message(F.voice)
async def voice_to_text(message: Message):
    file_id = message.voice.file_id

    file = await main.bot.get_file(file_id)
    file_path = file.file_path
    file_on_disk = Path("/home/capybara/dev/akaii_chatbot/Akaii-Telegram-bot/media/audio/", f"{file_id}.ogg")
    await main.bot.download_file(file_path, destination=file_on_disk)
    await message.reply("Аудио получено")

    text = stt.audio_to_text(file_on_disk)
    print(file_on_disk)
    if not text:
        text = "Формат документа не поддерживается"
    os.remove(file_on_disk)
    await message.reply(text + ".")

