from datetime import time
from typing import List, Optional

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship

from ..models.declarative_base import Base
from ..databases import Schema
from ..models.fixed_rule import FixedRule
from ..models.holiday import Holiday
from ..models.system import DaysIntEnum, DaysNameEnum
from ..models.work_rule import WorkRule


class PayRule(Base, Schema):
    __tablename__ = "pay_rule"

    pay_rule_id:               Mapped[int] = Column(Integer, primary_key=True, index=True)
    name:                      Mapped[str] = Column(String, unique=True)
    description:               Mapped[str] = Column(String)
    interpretation_rule_id:    Mapped[int] = Column(Integer, ForeignKey('interpretation_rule.interpretation_rule_id'), nullable=True)
    credit_holiday_default_id: Mapped[int] = Column(Integer, ForeignKey('credit_holiday_rule.holiday_rule_id'))
    fixed_rule_id:             Mapped[int] = Column(Integer, ForeignKey('fixed_rule.fixed_rule_id'), nullable=True)
    work_rule_default_id:      Mapped[int] = Column(Integer, ForeignKey('work_rule.work_rule_id'), nullable=True)
    calculate_projected_totals: Mapped[bool] = Column(Boolean)
    treat_planned_hour:        Mapped[bool] = Column(Boolean)
    enable:                    Mapped[bool] = Column(Boolean)

    holidays:                  Mapped[List["Holiday"]] = relationship("Holiday", secondary="pay_rule_r_holiday", lazy="joined", viewonly=True)
    asignation:                Mapped[List["PayRuleRWorkRule"]] = relationship("PayRuleRWorkRule", lazy="joined", order_by="PayRuleRWorkRule.order")

    holidays_r:                Mapped[List["PayRuleRHoliday"]] = relationship("PayRuleRHoliday", lazy="joined")

    fixed_rule: Mapped[Optional[FixedRule]]             = relationship("FixedRule", uselist=False, lazy="joined")
    work_rule_default: Mapped[Optional[WorkRule]]       = relationship("WorkRule", uselist=False, lazy="joined")

    @property
    def fixed_rule_name(self):
        return self.fixed_rule.name if self.fixed_rule else None

    @property
    def work_rule_default_name(self):
        return self.work_rule_default.name if self.work_rule_default else None

class PayRuleRHoliday(Base):
    __tablename__ = "pay_rule_r_holiday"

    pay_rule_id:     Mapped[int] = Column(Integer, ForeignKey('pay_rule.pay_rule_id'), primary_key=True, index=True)
    holiday_id:      Mapped[int] = Column(Integer, ForeignKey('holiday.holiday_id'), primary_key=True, index=True)

class PayRuleRWorkRule(Base, Schema):
    """ Regla de Asignación """

    __tablename__ = "pay_rule_r_work_rule"

    pay_rule_r_work_rule_id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    pay_rule_id:     Mapped[int] = Column(Integer, ForeignKey('pay_rule.pay_rule_id'))
    work_rule_id:    Mapped[int] = Column(Integer, ForeignKey('work_rule.work_rule_id'))
    start_hour:      Mapped[time] = Column(String)
    end_hour:        Mapped[time] = Column(String)
    min_shift:       Mapped[time] = Column(String)
    max_shift:       Mapped[time] = Column(String)
    _days_week:       Mapped[int] = Column("days_week", Integer)
    planned:         Mapped[bool] = Column(Boolean)
    unplanned:       Mapped[bool] = Column(Boolean)
    order:           Mapped[int] = Column(Integer)

    @property
    def days_week(self) -> list[DaysNameEnum]:
        ls = [v.name for v in DaysIntEnum if v & self._days_week]
        if len(ls) == 0:
            ls = []
        return ls

    @days_week.setter
    def days_week(self, value:list[DaysIntEnum]) -> None:
        self._days_week = 0
        for day in value:
            self._days_week |= DaysIntEnum[day].value