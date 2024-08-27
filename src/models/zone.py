import enum
from datetime import time
from typing import List

from sqlalchemy import Boolean, Column, Enum, ForeignKey, Integer, String, Time
from sqlalchemy.orm import Mapped, relationship

from ..models.declarative_base import Base
from ..databases import Schema
from ..models.system import DaysIntEnum, DaysNameEnum


class TypeZoneEnum(str, enum.Enum):
    consecutive_days_worked = 'consecutive_days_worked'
    holiday = 'holiday'
    week_days = 'week_days'
    diferential_daily_extend_zone_rule = 'diferential_daily_extend_zone_rule'
    diferential_weekly_extend_daily = 'diferential_weekly_extend_daily'

class HolidayZoneDefinedByEnum(str, enum.Enum):
    hours_in_the_holiday = 'hours_in_the_holiday'
    day_division_time = 'day_division_time'

class HolidayZoneDeductedTimeEnum(str, enum.Enum):
    none = 'none'
    hours_worked = 'hours_worked'
    full_credit = 'full_credit'

class HolidayZoneHoursWorkedBelongToEnum(enum.Enum):
    fixed_rule_value = 'fixed_rule_value'
    planned_day_of_entry = 'planned_day_of_entry'
    planned_day_of_departure = 'planned_day_of_departure'
    day_with_most_hours = 'day_with_most_hours'
    day_really_worked = 'day_really_worked'

class DiferentialQualifiersBasedByEnum(enum.Enum):
    real_punch = 'real_punch'
    schedule = 'schedule'

class WeekDaysApplyToEnum(enum.Enum):
    hours_worked = 'hours_worked'
    hours_to_day = 'hours_to_day'

class TypeConsecutiveEnum(enum.Enum):
    consecute_days = 'consecute_days'
    days_week   = 'days_week'

class Zone(Base, Schema):
    __tablename__ = "zone"

    zone_id:            Mapped[int] =                Column(Integer, primary_key=True, index=True)
    name:               Mapped[str] =                Column(String, index=True, unique=True)
    description:        Mapped[str] =                Column(String, index=True)
    type:               Mapped[TypeZoneEnum] =       Column(Enum(TypeZoneEnum))
    requires_approval:  Mapped[bool] =               Column(Boolean, default=False)
    enable:             Mapped[bool] =               Column(Boolean, default=True)


    __mapper_args__ = {"polymorphic_on": type}

    @property
    def id(self) -> int:
        return self.zone_id

class ConsecutiveDaysWorkedZone(Zone):
    __tablename__ = "consecutive_days_worked_extend_zone_rule"

    zone_id =                     Column(Integer, ForeignKey("zone.zone_id"), primary_key=True, index=True)
    day_amount =                  Column(Integer)
    min_hours =                   Column(Time)
    min_hours_last_day =          Column(Time)
    type_consecutive =            Column(Enum(TypeConsecutiveEnum))
    consecutive_days_numberday =  Column(Integer, nullable=True)
    consecutive_days_day_week =   Column(Enum(DaysNameEnum), nullable=True)
    days_week_restart_day =       Column(Enum(DaysNameEnum), nullable=True)

    sustitution_overtime: Mapped[List["OvertimeRule"]] = relationship("OvertimeRule", secondary="sustitution_overtime")

    __mapper_args__ = {
        "polymorphic_identity":  TypeZoneEnum.consecutive_days_worked
    }

class HolidayZone(Zone):
    __tablename__ = "holiday_extend_zone_rule"

    zone_id =                   Column(Integer, ForeignKey("zone.zone_id"), primary_key=True, index=True)
    defined_by =                Column(Enum(HolidayZoneDefinedByEnum))
    deducted_time =             Column(Enum(HolidayZoneDeductedTimeEnum))
    hours_worked_belong_to =    Column(Enum(HolidayZoneHoursWorkedBelongToEnum))

    holidays = relationship("Holiday", secondary="holiday_selected_r_holiday", lazy="subquery")

    __mapper_args__ = {
        "polymorphic_identity": TypeZoneEnum.holiday
    }


class HolidaySelectedHoliday(Base):
    __tablename__ = "holiday_selected_r_holiday"

    holiday_extend_zone_rule =  Column(Integer, ForeignKey("holiday_extend_zone_rule.zone_id"), primary_key=True, index=True)
    holiday_id =                Column(Integer, ForeignKey("holiday.holiday_id"), primary_key=True, index=True)

class WeekDays(Zone):
    __tablename__ = "week_days_extend_zone_rule"

    zone_id =       Column(Integer, ForeignKey("zone.zone_id"), primary_key=True, index=True)
    _days =         Column("days", Integer)
    applies_to =    Column(Enum(WeekDaysApplyToEnum))

    @property
    def days(self) -> list:
        ls = [v.name for v in DaysIntEnum if v & self._days]
        if len(ls) == 0:
            ls = []
        return ls

    @days.setter
    def days(self, value:list[DaysIntEnum]) -> None:
        self._days = 0
        for v in value:
            self._days |= v.value

    __mapper_args__ = {
        "polymorphic_identity": TypeZoneEnum.week_days
    }

class DiferentialType():
    start_hour:         Mapped[time] =                               Column(Time)
    end_hour:           Mapped[time] =                               Column(Time)
    min_hours_in_zone:  Mapped[time] =                               Column(Time)
    min_hours_in_shift: Mapped[time] =                               Column(Time)
    margin_early:       Mapped[time] =                               Column(Time)
    margin_late:        Mapped[time] =                               Column(Time)
    planned:            Mapped[bool] =                               Column(Boolean)
    based_by:           Mapped[DiferentialQualifiersBasedByEnum] =   Column(Enum(DiferentialQualifiersBasedByEnum), nullable=True)
    start_work_before:  Mapped[time] =                               Column(Time, nullable=True)
    start_work_after:   Mapped[time] =                               Column(Time, nullable=True)
    end_work_before:    Mapped[time] =                               Column(Time, nullable=True)
    end_work_after:     Mapped[time] =                               Column(Time, nullable=True)


class DiferentialDaily(Zone, DiferentialType):
    __tablename__ = "diferential_daily_extend_zone_rule"

    zone_id: Mapped[int] = Column(Integer, ForeignKey("zone.zone_id"), primary_key=True, index=True)

    __mapper_args__ = {
        "polymorphic_identity": TypeZoneEnum.diferential_daily_extend_zone_rule
    }

class DiferentialWeekendly(Zone, DiferentialType):
    __tablename__ = "diferential_weekendly_extend_daily"

    zone_id:    Mapped[int] =               Column(Integer, ForeignKey("zone.zone_id"), primary_key=True, index=True)
    start_day:  Mapped[DaysNameEnum] =      Column(Enum(DaysNameEnum))
    end_day:    Mapped[DaysNameEnum] =      Column(Enum(DaysNameEnum))

    __mapper_args__ = {
        "polymorphic_identity": TypeZoneEnum.diferential_weekly_extend_daily
    }