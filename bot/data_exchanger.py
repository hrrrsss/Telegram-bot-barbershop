from database.engine_db import async_session

from database.tables_db import Users



async def create_user(user_name: str, tg_id: int) -> None:
    async with async_session() as session:
        user = Users(tg_id=tg_id,
                     name=user_name)
        session.add(user)
        await session.commit()