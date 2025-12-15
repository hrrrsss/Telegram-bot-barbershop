from typing import Annotated
from datetime import datetime

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, DateTime, func

from bot.database.engine_db import Base


intpk = Annotated[int, mapped_column(primary_key=True)]

class Barbers(Base):
    __tablename__ = "barbers"

    barber_id: Mapped[intpk]
    barber_name: Mapped[str] = mapped_column(String(200))
    status: Mapped[bool]


class Services(Base):
    __tablename__ = "services"

    service_id: Mapped[intpk]
    service_name: Mapped[str] = mapped_column(String(300))


class Dates(Base):
    __tablename__ = "dates"

    date_id: Mapped[intpk]
    date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )