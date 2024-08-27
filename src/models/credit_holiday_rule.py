import enum
from typing import List

from sqlalchemy import Boolean, Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship

from ..models.declarative_base import Base

class PayCreditsLikeEnum(str, enum.Enum):
    how_if_work = 'Como si trabajara'
    in_pay_codes = 'En codigos de pagos'

class ConsiderOnExtratimeEnum(str, enum.Enum):
    paycode = 'paycode'
    always = 'always'
    never = 'never'

class ZoneHolidayDefinedByEnum(str, enum.Enum):
    hours_on_holiday_table = 'hours_on_holiday_table'
    division_hours_into_days = 'division_hours_into_days'

class HoursBelongEnum(str, enum.Enum):
    value_fixed_rule = 'value_fixed_rule'

class TimeDeductedFromHolidayCredit(str, enum.Enum):
    value_zone_rule = 'value_zone_rule'
    none = 'none'
    hours_worked = 'hours_worked'
    full_credit = 'full_credit'

class PlannedMoreShiftEnum(str, enum.Enum):
    use_first_shift = 'use_first_shift'
    use_sum_of_all_shifts = 'use_sum_of_all_shifts'

class CreditTypeEnum(str, enum.Enum):
    hours_from_schedule = 'hours_from_schedule'
    fixed_quantity_of_hours = 'fixed_quantity_of_hours'

class ShiftEquivalentToEnum(str, enum.Enum):
    shift_real_planned = 'Turno realmente planificado'
    all_shift_on_day_planned = 'Todo turno en el dia del turno planificad'


class CreditHolidayRule(Base):
    __tablename__ = "credit_holiday_rule"

    holiday_rule_id:                          Mapped[int]                            = Column(Integer, primary_key=True)
    name:                                     Mapped[str]                            = Column(String)
    description:                              Mapped[str]                            = Column(String)
    must_work_shift_before_holiday:           Mapped[bool]                           = Column(Boolean)
    must_work_shift_after_holiday:            Mapped[bool]                           = Column(Boolean)
    must_work_shift_before_or_after_holiday:  Mapped[bool]                           = Column(Boolean)
    must_work_shift_in_holiday:               Mapped[bool]                           = Column(Boolean)
    amount_hours:                             Mapped[str]                            = Column(String, nullable=True)
    shift_equivalent_to:                      Mapped[ShiftEquivalentToEnum]          = Column(Enum(ShiftEquivalentToEnum))
    credit_type:                              Mapped[CreditTypeEnum]                 = Column(Enum(CreditTypeEnum))
    if_planned_more_one_shift_in_day:         Mapped[PlannedMoreShiftEnum]           = Column(Enum(PlannedMoreShiftEnum))
    hours_belong:                             Mapped[HoursBelongEnum]                = Column(Enum(HoursBelongEnum))
    zone_holiday_defined_by:                  Mapped[ZoneHolidayDefinedByEnum]       = Column(Enum(ZoneHolidayDefinedByEnum))
    pay_credits_like:                         Mapped[PayCreditsLikeEnum]             = Column(Enum(PayCreditsLikeEnum))
    work_rule_id:                             Mapped[int]                            = Column(Integer, ForeignKey('work_rule.work_rule_id'), nullable=True)
    consider_on_extratime_limit:              Mapped[ConsiderOnExtratimeEnum]        = Column(Enum(ConsiderOnExtratimeEnum), nullable=True)
    consider_on_extratime_consecutive_days:   Mapped[ConsiderOnExtratimeEnum]        = Column(Enum(ConsiderOnExtratimeEnum), nullable=True)
    paycode_extratime_limit_id:               Mapped[int]                            = Column(Integer, ForeignKey('paycode.paycode_id'), nullable=True)
    paycode_extratime_consecutive_days_id:    Mapped[int]                            = Column(Integer, ForeignKey('paycode.paycode_id'), nullable=True)
    enable:                                   Mapped[bool]                           = Column(Boolean, default=True)
    time_deducted_from_holiday_credit:        Mapped[TimeDeductedFromHolidayCredit]  = Column(Enum(TimeDeductedFromHolidayCredit))

    paycode_extratime_limit:                  Mapped['Paycode']                      = relationship('Paycode', foreign_keys=[paycode_extratime_limit_id], lazy="joined", overlaps="paycodes", viewonly=True)
    paycode_extratime_consecutive_days:       Mapped['Paycode']                      = relationship('Paycode', foreign_keys=[paycode_extratime_limit_id], lazy="joined", overlaps="paycodes")

    paycodes:                                 Mapped[List["Paycode"]]                = relationship('Paycode', secondary='credit_holiday_rule_r_paycode', lazy="joined", overlaps="credit_holiday_rules")


class CreditHolidayRuleRPaycode(Base):
    __tablename__ = "credit_holiday_rule_r_paycode"

    holiday_rule_id:                 Mapped[int] = Column(Integer, ForeignKey('credit_holiday_rule.holiday_rule_id'), primary_key=True)
    paycode_id:                      Mapped[int] = Column(Integer, ForeignKey('paycode.paycode_id'), primary_key=True)