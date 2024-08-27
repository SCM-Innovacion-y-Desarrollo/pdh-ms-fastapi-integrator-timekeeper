import enum
from datetime import time

from sqlalchemy import Boolean, Column, Enum, Integer, String, Time
from sqlalchemy.orm import Mapped

from ..models.declarative_base import Base
from ..databases import Schema

class StartBreakByEnum(str, enum.Enum):
    midnight = "midnight"
    planned_start_time = "planned_start_time"
    real_start_time = "real_start_time"


class BreakRule(Base, Schema):
    __tablename__ = "break_rule"

    break_rule_id:                   Mapped[int]         = Column(Integer, primary_key=True)
    name:                            Mapped[str]         = Column(String)
    duration_normal:                 Mapped[time]        = Column(Time)
    duration_medio:                  Mapped[time]        = Column(Time)
    duration_max:                    Mapped[time]        = Column(Time)
    use_rounding_punch_unplan:       Mapped[bool]         = Column(Boolean)
    break_short_round:               Mapped[time]        = Column(Time)
    break_short_grace_period:        Mapped[time]        = Column(Time)
    break_intermedio_round:          Mapped[time]        = Column(Time)
    break_intermedio_grace_period:   Mapped[time]        = Column(Time)
    break_long_round:                Mapped[time]        = Column(Time)
    break_long_grace_period:         Mapped[time]        = Column(Time)
    start_break_after:               Mapped[time]        = Column(Time)
    start_break_before:              Mapped[time]        = Column(Time)
    start_break_by:                  Mapped[StartBreakByEnum]         = Column(Enum(StartBreakByEnum))
    start_break_amount_pay:          Mapped[time]        = Column(Time)
    start_break_limit_except_short:  Mapped[time]        = Column(Time)
    start_break_limit_except_long:   Mapped[time]        = Column(Time)
    enable:                          Mapped[bool]        = Column(Boolean)

