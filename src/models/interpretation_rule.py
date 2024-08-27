import enum

from sqlalchemy import Boolean, Column, Enum, Integer, String
from sqlalchemy.orm import Mapped

from ..models.declarative_base import Base


class PunchRestrictionEnum(str, enum.Enum):
    complete = 'complete'
    simple = 'simple'


class InterpretationRule(Base):
    __tablename__ = "interpretation_rule"

    interpretation_rule_id:          Mapped[int]                            = Column(Integer, primary_key=True)
    name:                            Mapped[str]                            = Column(String)
    description:                     Mapped[str]                            = Column(String)
    punch_restriction:               Mapped[PunchRestrictionEnum]           = Column(Enum(PunchRestrictionEnum))
    allow_substitution:              Mapped[bool]                           = Column(Boolean)
    early_start_margin:              Mapped[str]                            = Column(String)
    early_start_restriction:         Mapped[str]                            = Column(String)
    late_start_restriction:          Mapped[str]                            = Column(String, nullable=True)
    late_start_margin:               Mapped[str]                            = Column(String)
    omitted_output_margin:           Mapped[str]                            = Column(String)
    brake_maximum_output :           Mapped[str]                            = Column(String, nullable=True)
    brake_minimum_refreshment_ :     Mapped[str]                            = Column(String, nullable=True)
    brake_impose_reset :             Mapped[bool]                           = Column(Boolean, nullable=True)
    brake_early_rest_start :         Mapped[str]                            = Column(String, nullable=True)
    brake_late_rest_start_margin :   Mapped[str]                            = Column(String, nullable=True)
    brake_late_rest_end_margin :     Mapped[str]                            = Column(String, nullable=True)
    start_early_end_restriction :    Mapped[str]                            = Column(String, nullable=True)
    end_early_end_restriction :      Mapped[str]                            = Column(String, nullable=True)
    late_end_restriction :           Mapped[str]                            = Column(String)
    punch_out_limit_omitted :        Mapped[str]                            = Column(String)
    restrict_unplanned_punch_in:     Mapped[bool]                           = Column(Boolean, nullable=True)
    unplanned_shift_duration :       Mapped[str]                            = Column(String)
    enable:                          Mapped[bool]                           = Column(Boolean, default=True)
