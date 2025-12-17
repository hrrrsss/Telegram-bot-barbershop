import asyncio

import logging
from redis.asyncio import Redis
from aiogram.fsm.storage.redis import RedisStorage
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config.config import settings
from handlers.user_hd import (start_hd, appointment_hd)


logger = logging.getLogger(__name__)


async def main():

    logging.basicConfig(
        level=logging.getLevelName(level=settings.log_level),
        format=settings.log_format,
    )
    logger.info("Starting bot")

    r = Redis(host=settings.R_HOST,
              port=settings.R_PORT,
              db=settings.R_DB)

    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.
                                                HTML)
    )
    dp = Dispatcher(storage=RedisStorage(redis=r))


    dp.include_router(start_hd.start_router)
    dp.include_router(appointment_hd.appointment_router)


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())