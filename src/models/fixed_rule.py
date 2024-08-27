import enum
from datetime import date, time

from sqlalchemy import Column, Date, Enum, Integer, String, Time
from sqlalchemy.orm import Mapped

from ..models.declarative_base import Base


class TypePaymentPeriodEnum(str, enum.Enum):
    day = 'day'
    bimonthly = 'bimonthly'
    monthly = 'monthly'

class HoursBelongToEnum(str, enum.Enum):
    planned_entry_day = "Dia de entrada planificado"
    planned_departure_day = "Dia de salida planificado"
    day_with_most_hours = "Dia con mayoria de horas"
    really_worked_day = "Dia realmente trabajado"


class FixedRule(Base):
    __tablename__ = "fixed_rule"


    fixed_rule_id:                   Mapped[int]                            = Column(Integer, primary_key=True)
    name:                            Mapped[str]                            = Column(String)
    type_payment_period:             Mapped[TypePaymentPeriodEnum]          = Column(Enum(TypePaymentPeriodEnum))
    date_reference:                  Mapped[date]                           = Column(Date)
    days:                            Mapped[int]                            = Column(Integer, nullable=True)
    day_reference:                   Mapped[int]                            = Column(Integer)
    day_division_hours:              Mapped[time]                           = Column(Time, default="00:00")
    hours_belong_to:                 Mapped[HoursBelongToEnum]              = Column(Enum(HoursBelongToEnum))
    enable:                          Mapped[bool]                           = Column(Integer, default=True)
    description:                     Mapped[str]                            = Column(String, nullable=True)


