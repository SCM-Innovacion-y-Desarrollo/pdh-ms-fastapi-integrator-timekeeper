import enum
from datetime import datetime, time
from typing import List

from sqlalchemy import (Boolean, Column, DateTime, Enum, ForeignKey, Integer,
                        String, Time)
from sqlalchemy.orm import Mapped, relationship

from ..models.declarative_base import Base
from ..databases import Schema
from ..models.system import DaysNameEnum


class ValidityPeriodEnum(str, enum.Enum):
    day = 'day'
    week = 'week'
    fortnight = 'fortnight'

class OvertimeRule(Base, Schema):
    __tablename__ = "overtime_rule"

    overtime_rule_id:       Mapped[int] =                   Column(Integer, primary_key=True, index=True)
    name:                   Mapped[str] =                   Column(String)
    description:            Mapped[str] =                   Column(String)
    overtime_start:         Mapped[str] =                   Column(String)
    validity_period:        Mapped[ValidityPeriodEnum] =    Column(Enum(ValidityPeriodEnum))
    restart_date:           Mapped[datetime] =              Column(DateTime)
    restart_week:           Mapped[DaysNameEnum] =          Column(Enum(DaysNameEnum))
    min_hour_calification:  Mapped[time] =                  Column(Time)
    required_approval:      Mapped[bool] =                  Column(Boolean)
    enable:                 Mapped[bool] =   Column(Boolean, nullable=False, default=True)

    paycodes:               Mapped[List["Paycode"]] = relationship("Paycode", secondary="overtime_rule_r_paycode")
    overtime_rule_r_paycodes: Mapped[List["OvertimeRuleRPaycode"]] = relationship("OvertimeRuleRPaycode", overlaps="paycodes")

    @property
    def id(self) -> int:
        return self.overtime_rule_id




class OvertimeRuleRPaycode(Base):
    __tablename__ = "overtime_rule_r_paycode"

    overtime_rule_id:   Mapped[int] =    Column(Integer, ForeignKey('overtime_rule.overtime_rule_id'), primary_key=True, index=True)
    paycode_id:         Mapped[int] =    Column(Integer, ForeignKey('paycode.paycode_id'), primary_key=True, index=True)


class SustitutionOvertime(Base):
    __tablename__ = "sustitution_overtime"

    overtime_rule_id:   Mapped[int] =    Column(Integer, ForeignKey('overtime_rule.overtime_rule_id'), primary_key=True, index=True)
    zone_id:            Mapped[int] =    Column(Integer, ForeignKey('zone.zone_id'), primary_key=True, index=True)