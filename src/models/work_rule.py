from typing import List, Optional

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship

from ..models.declarative_base import Base
from ..models.exception_rule import ExceptionRule
from ..models.paycodes_distibution import PaycodesDistribution
from ..models.rounding_rule import RoundingRule


class WorkRule(Base):
    __tablename__ = "work_rule"

    work_rule_id:              Mapped[int] = Column(Integer, primary_key=True, index=True)
    name:                      Mapped[str] = Column(String)
    description:               Mapped[str] = Column(String)
    excepcion_rule_id:         Mapped[int] = Column(Integer, ForeignKey('exception_rule.exception_rule_id'), nullable=True)
    paycodes_distribution_id:  Mapped[int] = Column(Integer, ForeignKey('paycodes_distribution.paycodes_distribution_id'), nullable=True)
    rounding_rule_id:          Mapped[int] = Column(Integer, ForeignKey('rounding_rule.rounding_rule_id'), nullable=True)
    enable:                    Mapped[bool] = Column(Integer, default=True)

    bonus:                     Mapped[List["WorkRuleRBonus"]] =              relationship("BonusRule", secondary="work_rule_r_bonus", lazy="joined")
    break_rules:               Mapped[List["WorkRuleRBreak"]] =              relationship("BreakRule", secondary="work_rule_r_break_rule", lazy="joined")
    overtime_rules:            Mapped[List["WorkRuleROvertime"]] =           relationship("OvertimeRule", secondary="work_rule_r_overtime", lazy="joined")
    zones:                     Mapped[List["WorkRuleRZone"]] =               relationship("Zone", secondary="work_rule_r_zone", lazy="joined")
    schedule_desviation_rules: Mapped[List["WorkRuleRScheduleDesviation"]] = relationship("ScheduleDesviationRule", secondary="work_rule_r_schedule_desviation_rule", lazy="joined")

    exception_rule:            Mapped[Optional[ExceptionRule]] =             relationship("ExceptionRule", uselist=False)
    rounding_rule:             Mapped[Optional[RoundingRule]] =              relationship("RoundingRule", uselist=False)
    paycodes_distribution:     Mapped[Optional[PaycodesDistribution]] =      relationship("PaycodesDistribution", uselist=False)

    @property
    def exception_rule_name(self):
        return self.exception_rule.name if self.exception_rule else None

    @property
    def paycodes_distribution_name(self):
        return self.paycodes_distribution.name if self.paycodes_distribution else None

    @property
    def rounding_rule_name(self):
        return self.rounding_rule.name if self.rounding_rule else None


class WorkRuleRBonus(Base):
    __tablename__ = "work_rule_r_bonus"

    work_rule_id:              Mapped[int] = Column(Integer, ForeignKey('work_rule.work_rule_id'), primary_key=True, index=True)
    bonus_rule_id:             Mapped[int] = Column(Integer, ForeignKey('bonus_rule.bonus_rule_id'), primary_key=True, index=True)

class WorkRuleRBreak(Base):
    __tablename__ = "work_rule_r_break_rule"

    work_rule_id:              Mapped[int] = Column(Integer, ForeignKey('work_rule.work_rule_id'), primary_key=True, index=True)
    break_rule_id:             Mapped[int] = Column(Integer, ForeignKey('break_rule.break_rule_id'), primary_key=True, index=True)

class WorkRuleROvertime(Base):
    __tablename__ = "work_rule_r_overtime"

    work_rule_id:              Mapped[int] = Column(Integer, ForeignKey('work_rule.work_rule_id'), primary_key=True, index=True)
    overtime_rule_id:          Mapped[int] = Column(Integer, ForeignKey('overtime_rule.overtime_rule_id'), primary_key=True, index=True)

class WorkRuleRZone(Base):
    __tablename__ = "work_rule_r_zone"

    work_rule_id:              Mapped[int] = Column(Integer, ForeignKey('work_rule.work_rule_id'), primary_key=True, index=True)
    zone_id:                   Mapped[int] = Column(Integer, ForeignKey('zone.zone_id'), primary_key=True, index=True)

class WorkRuleRScheduleDesviation(Base):
    __tablename__ = "work_rule_r_schedule_desviation_rule"

    work_rule_id:              Mapped[int] = Column(Integer, ForeignKey('work_rule.work_rule_id'), primary_key=True, index=True)
    schedule_desviation_rule_id: Mapped[int] = Column(Integer, ForeignKey('schedule_desviation_rule.schedule_desviation_rule_id'), primary_key=True, index=True)