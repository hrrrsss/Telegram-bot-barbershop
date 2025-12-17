from typing import Annotated
from datetime import (datetime, 
                      date, 
                      time)
import pytz
from enum import Enum

from sqlalchemy.orm import (mapped_column, 
                            Mapped, 
                            relationship)
from sqlalchemy import (String, DateTime, 
                        ForeignKey, BigInteger, 
                        Integer, Time)
from sqlalchemy import Enum as SQLEnum

from database.engine_db import Base


intpk = Annotated[int, mapped_column(primary_key=True)]

#auxiliary func
def moscow_time():
    moscow_tz = pytz.timezone("Europe/Moscow")

    return datetime.now(moscow_tz)


class Users(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    tg_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        index=True,
        nullable=False
    )
    name: Mapped[str] = mapped_column(String(200))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=moscow_time,
        nullable=False
    )


class Admins(Base):
    __tablename__ = "admins"

    id: Mapped[intpk]
    tg_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        index=True,
        nullable=False
    )


class Barbers(Base):
    __tablename__ = "barbers"

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(String(200))
    is_active: Mapped[bool]


class Services(Base):
    __tablename__ = "services"

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(String(300))
    duration: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )
    is_active: Mapped[bool]


class Barber_services(Base):
    __tablename__ = "barber_services"

    id: Mapped[intpk]
    barber_id: Mapped[int] = mapped_column(
        ForeignKey("barbers.id"),
        nullable=False
    )
    service_id: Mapped[int] = mapped_column(
        ForeignKey("services.id"),
        nullable=False
    )


class AppointmentStatus(str, Enum):
    ACTIVE = "active"
    CANCELED = "canceled"
    COMPLETED = "completed"


class Appointments(Base):
    __tablename__ = "appointments"

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )
    barber_id: Mapped[int] = mapped_column(
        ForeignKey("barbers.id"),
        nullable=False
    )
    service_id: Mapped[int] = mapped_column(
        ForeignKey("services.id"),
        nullable=False
    )
    date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=moscow_time,
        nullable=False
    )
    time_start: Mapped[time] = mapped_column(Time, 
                                             nullable=False)
    time_end: Mapped[time] = mapped_column(Time,
                                           nullable=False)
    status: Mapped[AppointmentStatus] = mapped_column(
        SQLEnum(AppointmentStatus,
                name="appointment_status"),
        nullable=False,
        default=AppointmentStatus.ACTIVE
    )
    when_created: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=moscow_time,
        nullable=False
    )


class BarberSchedule(Base):
    __tablename__ = "barber_schedule"

    id: Mapped[intpk]
    barber_id: Mapped[int] = mapped_column(
        ForeignKey("barbers.id"),
        nullable=False
    )
    weekday: Mapped[int] = mapped_column(
        Integer, nullable=False
    )