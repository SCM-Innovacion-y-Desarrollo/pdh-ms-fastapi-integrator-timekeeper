import enum
from typing import List, Optional

from sqlalchemy import (Boolean, Column, ForeignKey, Integer, String)
from sqlalchemy.orm import Mapped, object_session, relationship

from ..models.declarative_base import Base
from ..databases import Schema
from ..models.overtime_rule import OvertimeRule
from ..models.schedule_desviation_rule import ScheduleDesviationRule
from ..models.zone import Zone


def get_class_table(element) -> str:
    """Get the name of the table by the element """
    tipos = [OvertimeRule, Zone, ScheduleDesviationRule]
    for t in tipos:
        if t.__name__ == element:
            return t
    return None

class CombinationRule(Base, Schema):
    __tablename__ = "combination_rule"

    combination_rule_id:       Mapped[int] =    Column(Integer, primary_key=True, index=True)
    name:                      Mapped[str] =    Column(String)
    description:               Mapped[str] =    Column(String)
    default:                   Mapped[bool] =   Column(Boolean)


    overtime_rules:            Mapped[List["OvertimeRule"]] =           relationship("OvertimeRule", secondary="combination_rule_r_overtime", lazy="joined")
    zones:                     Mapped[List["Zone"]] =                   relationship("Zone", secondary="combination_rule_r_zone", lazy="joined")
    schedule_desviation_rules: Mapped[List["ScheduleDesviationRule"]] = relationship("ScheduleDesviationRule", secondary="combination_rule_r_schedule_desviation_rule", lazy="joined")

    # combinations:             Mapped[List["Combinations"]] =                relationship("Combinations")
    combination_overtime:                              Mapped[List["CombinationRuleROvertime"]] =                relationship("CombinationRuleROvertime", lazy="joined", overlaps="overtime_rules")
    combination_zones:                                 Mapped[List["CombinationRuleRZone"]] =                    relationship("CombinationRuleRZone", lazy="joined", overlaps="zones")
    combination_schedule_desviation_rules:             Mapped[List["CombinationRuleRScheduleDesviation"]] =      relationship("CombinationRuleRScheduleDesviation", lazy="joined", overlaps="schedule_desviation_rules")


class CombinationRuleROvertime(Base):
    __tablename__ = "combination_rule_r_overtime"

    combination_rule_id:     Mapped[int] =    Column(Integer, ForeignKey('combination_rule.combination_rule_id'), primary_key=True, index=True)
    overtime_rule_id:        Mapped[int] =    Column(Integer, ForeignKey('overtime_rule.overtime_rule_id'), primary_key=True, index=True)

class CombinationRuleRZone(Base):
    __tablename__ = "combination_rule_r_zone"

    combination_rule_id:     Mapped[int] =    Column(Integer, ForeignKey('combination_rule.combination_rule_id'), primary_key=True, index=True)
    zone_id:                 Mapped[int] =    Column(Integer, ForeignKey('zone.zone_id'), primary_key=True, index=True)

class CombinationRuleRScheduleDesviation(Base):
    __tablename__ = "combination_rule_r_schedule_desviation_rule"

    combination_rule_id:         Mapped[int] =    Column(Integer, ForeignKey('combination_rule.combination_rule_id'), primary_key=True, index=True)
    schedule_desviation_rule_id: Mapped[int] =    Column(Integer, ForeignKey('schedule_desviation_rule.schedule_desviation_rule_id'), primary_key=True, index=True)


class CombinationDefaultEnum(str, enum.Enum):
    """Combination Default Enum"""
    overtime = 'overtime'
    zone = 'zone'
    schedule_desviation = 'schedule_desviation'

class Combinations(Base):
    """Combinations Model"""
    __tablename__ = "combinations"

    def __str__(self):
        return f'{self.type_a}({self.id_a}) {self.type_b}({self.id_b}) D{self.default}'

    id:                             Mapped[int] = Column(Integer, primary_key=True, index=True)
    combination_rule_id:            Mapped[Optional[int]] = Column(Integer, ForeignKey('combination_rule.combination_rule_id'), index=True, nullable=False)
    id_a:                           Mapped[Optional[int]] = Column(Integer, nullable=False)
    id_b:                           Mapped[Optional[int]] = Column(Integer, nullable=False)
    type_a:                         Mapped[Optional[str]] = Column(String, nullable=False)
    type_b:                         Mapped[Optional[str]] = Column(String, nullable=False)
    default:                        Mapped[Optional[str]] = Column(String, nullable=True)

    @property
    def a(self):
        """Get the object A"""
        session = object_session(self)
        return session.query(get_class_table(self.type_a)).get(self.id_a)

    @property
    def b(self):
        """Get the object B"""
        session = object_session(self)
        return session.query(get_class_table(self.type_b)).get(self.id_b)

    @property
    def predeterminado(self):
        """Get the default object"""
        if not self.default:
            return None

        if self.default == "a":
            return self.a
        else:
            return self.b

    @property
    def no_predeterminado(self):
        """Get the no default object"""
        if not self.default:
            return None

        if self.default == "a":
            return self.b
        else:
            return self.a
