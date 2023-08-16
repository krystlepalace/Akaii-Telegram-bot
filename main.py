from decouple import config
import asyncio
from aiogram import Bot, Dispatcher
from handlers import base, callback_query, administrative, content_filters
from utils.commands import set_commands


TOKEN = config("BOT_TOKEN")
animations_allowed = False

bot = Bot(token=TOKEN)

# Bot startup function
async def main():
    dp = Dispatcher()
    dp.include_routers(
            base.router, 
            callback_query.router,
            administrative.router,
            content_filters.router,
            )
    
    # set commands
    await set_commands(bot)
    # start the bot
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
