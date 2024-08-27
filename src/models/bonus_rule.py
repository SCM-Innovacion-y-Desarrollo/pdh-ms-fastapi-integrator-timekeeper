import enum
from datetime import time

from sqlalchemy import Boolean, Column, Enum, ForeignKey, Integer, String, Time
from sqlalchemy.orm import Mapped

from ..models.declarative_base import Base
from ..models.system import DaysIntEnum, DaysNameEnum


class TimePeriodEnum(str, enum.Enum):
    shift = "shift"
    week = "week"
    pay_period = "pay_period"

class BonusActivateByEnum(str, enum.Enum):
    shift_duration = "shift_duration"
    hour_day = "hour_day"
    paycode = "paycode"

class BonusRule(Base):
    __tablename__ = "bonus_rule"

    bonus_rule_id:              Mapped[int] =                 Column(Integer, primary_key=True, index=True)
    name:                       Mapped[str] =                 Column(String)
    description:                Mapped[str] =                 Column(String)
    amount:                     Mapped[time] =                Column(Time)
    _days_in_week:              Mapped[int] =                 Column("days_in_week", Integer)
    is_exception:               Mapped[bool] =                Column(Boolean)
    paycode_id:                 Mapped[int] =                 Column(Integer, ForeignKey('paycode.paycode_id'))
    break_id:                   Mapped[int] =                 Column(Integer, ForeignKey('break_rule.break_rule_id'))
    allow_cancel_in_timesheet:  Mapped[bool] =                Column(Boolean)
    use_shift_restriction:      Mapped[bool] =                Column(Boolean)
    start_shift_restriction:    Mapped[time] =                Column(Time)
    end_shift_restriction:      Mapped[time] =                Column(Time)
    activate_by:                Mapped[BonusActivateByEnum] = Column(Enum(BonusActivateByEnum))
    enable:                     Mapped[bool] =                Column(Boolean, default=True)

    __mapper_args__ = {"polymorphic_on": activate_by}


    @property
    def days_in_week(self) -> list:
        ls = [v.name for v in DaysIntEnum if v & self._days_in_week]
        if len(ls) == 0:
            ls = []
        return ls

    @days_in_week.setter
    def days_in_week(self, value:list[DaysIntEnum]) -> None:
        self._days_in_week = 0
        for v in value:
            self._days_in_week |= v

class HourDayExtendBonusRule(BonusRule):
    __tablename__ = "hour_day_extend_bonus_rule"

    bonus_rule_id:  Mapped[int] =  Column(Integer, ForeignKey('bonus_rule.bonus_rule_id'), primary_key=True, index=True)
    hour:           Mapped[time] = Column(Time)

    __mapper_args__ = {
        "polymorphic_identity":  BonusActivateByEnum.hour_day
    }

class ShiftDurationExtendBonusRule(BonusRule):
    __tablename__ = "shift_duration_extend_bonus_rule"

    bonus_rule_id:                          Mapped[int] =  Column(Integer, ForeignKey('bonus_rule.bonus_rule_id'), primary_key=True, index=True)
    use_limit_hour_shift_round:             Mapped[bool] = Column(Boolean)
    exception_short_break_unqualif_break:   Mapped[bool] = Column(Boolean)
    min_interval_qualif:                    Mapped[time] = Column(Time)
    min_duration_shift_to_activate:         Mapped[time] = Column(Time)
    max_duration_shift_to_activate:         Mapped[time] = Column(Time, default="99:59")
    location:                               Mapped[time] = Column(Time, default=time(4, 0, 0))
    activate_if_location_match_or_after:    Mapped[time] = Column(Time)
    activate_if_location_is_befora:         Mapped[time] = Column(Time)

    __mapper_args__ = {
        "polymorphic_identity":  BonusActivateByEnum.shift_duration
    }

class ActiveByPaycodeExtendBonusRule(BonusRule):
    __tablename__ = "active_by_paycode_extend_bonus_rule"

    bonus_rule_id:                  Mapped[int] =              Column(Integer, ForeignKey('bonus_rule.bonus_rule_id'), primary_key=True, index=True)
    active_paycode_id:              Mapped[int] =              Column(Integer, ForeignKey('paycode.paycode_id'))
    minimum:                        Mapped[time] =             Column(Time)
    maximum:                        Mapped[time] =             Column(Time, default="999:00")
    time_period:                    Mapped[TimePeriodEnum] =   Column(Enum(TimePeriodEnum))
    achieve_requirements_for_shift: Mapped[bool] =             Column(Boolean)
    shifts_required:                Mapped[int] =              Column(Integer, nullable=True)
    start_day_week:                 Mapped[DaysNameEnum] =     Column(Enum(DaysNameEnum), nullable=True)

    __mapper_args__ = {
        "polymorphic_identity":  BonusActivateByEnum.paycode
    }