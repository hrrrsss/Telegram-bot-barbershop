import asyncio

from bot.database.engine_db import engine, Base
from bot.database.tables_db import Barbers, Services, Users # Обязательно нужно импортировать все модели


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    print("Таблицы созданы")

asyncio.run(create_tables())