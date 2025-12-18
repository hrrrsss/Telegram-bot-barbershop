from sqlalchemy import select
from database.engine_db import async_session
from database.tables_db import (Users, Appointments,
                                Barbers, BarberServices,
                                Services)


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
    

async def get_barbers() -> list[tuple]:
    async with async_session() as session:
        check = await session.execute(
            select(Barbers.id, Barbers.name)
            .where(Barbers.is_active == True)
        )

        result = check.all()
        return result
    

async def get_service(barber_id: int) -> list[tuple]:
    async with async_session() as session:
        result = await session.execute(
            select(Services.id, Services.name)
            .join(BarberServices, Services.id == BarberServices.service_id)
            .where(BarberServices.barber_id == barber_id,
                   Services.is_active == True)
        )
        return result.all()