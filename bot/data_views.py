from sqlalchemy import select
from database.engine_db import async_session
from database.tables_db import (Users, Appointments,
                                Barbers)


async def get_user_id(tg_id: int) -> bool:
    async with async_session() as session:
        check = await session.execute(
            select(Users.id).
            where(Users.tg_id == tg_id)
            )
        
        result = check.scalar_one_or_none()
        return result
    

async def get_appointments(id: int) -> list[Appointments]:  # потом пересмотреть какой тип
    async with async_session() as session:
        check = await session.execute(
            select(Appointments.barber_id,
                       Appointments.service_id,
                       Appointments.date,
                       Appointments.time_start,
                       Appointments.time_end
                       ).where(Appointments.user_id == id))
        result = check.scalar_one_or_none()
        return result
    

async def get_barbers() -> list[Barbers]:
    async with async_session() as session:
        check = await session.execute(
            select(Barbers.name)
            .where(Barbers.is_active == True)
        )

        result = check.scalars().all()
        return result