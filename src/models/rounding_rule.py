import enum
from datetime import time
from typing import List

from sqlalchemy import Boolean, Column, Enum, ForeignKey, Integer, String, Time
from sqlalchemy.orm import Mapped, relationship

from ..models.declarative_base import Base


class TypePunchOmitedRoundingEnum(str, enum.Enum):
    totals_real_projected = "totals_real_projected"
    only_totals_projected = "only_totals_projected"

class RoundingRule(Base):
    __tablename__ = "rounding_rule"

    rounding_rule_id:    Mapped[int] =    Column(Integer, primary_key=True, index=True)
    name:                Mapped[str] =    Column(String)
    description:         Mapped[str] =    Column(String)
    enable:              Mapped[bool] =   Column(Boolean, default=True)

    config_punch_r_rounding_rule: Mapped[List["RoundingConfigPunchRRoundingRule"]] = relationship("RoundingConfigPunchRRoundingRule", backref="rounding_rule", uselist=True, lazy="joined")
    rounding_config_unplan_r_rounding_rule: Mapped["RoundingConfigUnplanRRoundingRule"] = relationship("RoundingConfigUnplanRRoundingRule", backref="rounding_rule", uselist=False, lazy="joined")
    rounding_config_punch_omited_r_rounding_rule: Mapped["RoundingConfigPunchOmitedRRoundingRule"] = relationship("RoundingConfigPunchOmitedRRoundingRule", backref="rounding_rule", uselist=False, lazy="joined")

class RoundingConfigPunchRRoundingRule(Base):
    __tablename__ = "rounding_config_punch_r_rounding_rule"

    rounding_rule_id:      Mapped[int] =    Column(Integer, ForeignKey('rounding_rule.rounding_rule_id'), primary_key=True, index=True)
    in_out:                Mapped[bool] =    Column(Boolean, primary_key=True, index=True, comment="In = 1 , Out = 0")
    early_late:            Mapped[bool] =    Column(Boolean, primary_key=True, index=True, comment="Early = 1 , Late = 0")
    change_point:          Mapped[time] =    Column(Time, nullable=True)
    rounding_extern:       Mapped[time] =    Column(Time, nullable=True)
    rounding_intern:       Mapped[time] =    Column(Time, nullable=True)
    grace_period_extern:   Mapped[time] =    Column(Time, nullable=True)
    grace_period_intern:   Mapped[time] =    Column(Time, nullable=True)

class RoundingConfigUnplanRRoundingRule(Base):
    __tablename__ = "rounding_config_unplan_r_rounding_rule"

    rounding_rule_id:      Mapped[int] =    Column(Integer, ForeignKey('rounding_rule.rounding_rule_id'), primary_key=True, index=True)
    rounding_entry:        Mapped[time] =    Column(Time, nullable=True)
    grace_period_entry:    Mapped[time] =    Column(Time, nullable=True)
    rounding_exit:         Mapped[time] =    Column(Time, nullable=True)
    grace_period_exit:     Mapped[time] =    Column(Time, nullable=True)
    rounding_trans:        Mapped[time] =    Column(Time, nullable=True)
    grace_period_trans:    Mapped[time] =    Column(Time, nullable=True)

class RoundingConfigPunchOmitedRRoundingRule(Base):
    __tablename__ = "rounding_config_punch_omited_r_rounding_rule"

    rounding_rule_id:      Mapped[int] =    Column(Integer, ForeignKey('rounding_rule.rounding_rule_id'), primary_key=True, index=True)
    planified:             Mapped[bool] =    Column(Boolean)
    type:                  Mapped[TypePunchOmitedRoundingEnum] =    Column(Enum(TypePunchOmitedRoundingEnum), nullable=True)
    is_exception:          Mapped[bool] =    Column(Boolean, nullable=True)
