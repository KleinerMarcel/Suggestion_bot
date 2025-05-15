import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = "__Токен_вашего_бота__"  #Replace with your bot's token (you can make a separate file for the token and ID, but I decided not to bother)
ADMIN_IDS = [_ID_Админов_]  #Replace admin IDs
RULES_TEXT = RULES_TEXT = (
    "*Правила общения с гаргульями*\n\n"
    "• Сюда пишете ваши правила.\n"
    "• Ну и вообще все что хотите чтобы выдавалось на /rules.\n"
) #Write your rules here

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "Доброго времени. Я Гаргулья, ты можешь нашептать мне на ухо, и я передам этот секрет другим гаргульям."
    )

@dp.message(Command("rules"))
async def rules_handler(message: Message):
    await message.answer(RULES_TEXT) #Handler for the /rules command to send rules to the user

@dp.message()
async def forward_to_admins(message: Message):
    
    #Processing forwarded audio files
    if message.forward_from or message.forward_from_chat:
        if message.audio:
            audio_id = message.audio.file_id
            caption = message.caption or "Гаргулья принесла песнь"
            for admin_id in ADMIN_IDS:
                await bot.send_audio(admin_id, audio_id, caption=caption)
            await message.answer("Гаргульи услышали песнь")
            return

    #Photo processing
    if message.photo:
        photo = message.photo[-1].file_id  # Берем фото лучшего качества
        caption = message.caption or "Гаргулья принесла рисунок"
        for admin_id in ADMIN_IDS:
            await bot.send_photo(admin_id, photo, caption=caption)

    # Word processing
    elif message.text:
        for admin_id in ADMIN_IDS:
            await bot.send_message(admin_id, f"Гаргулья нашептала:\n\n{message.text}")
    
    await message.answer("Гаргульи шепчутся...")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())