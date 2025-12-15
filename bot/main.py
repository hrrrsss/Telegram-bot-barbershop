import asyncio

import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config.config import settings
from handlers.user_hd import start_hd


logger = logging.getLogger(__name__)


async def main():

    logging.basicConfig(
        level=logging.getLevelName(level=settings.log_level),
        format=settings.log_format,
    )
    logger.info("Starting bot")

    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()


    dp.include_router(start_hd.start_router)


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())