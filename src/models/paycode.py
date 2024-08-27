import enum

from sqlalchemy import (Boolean, Column, Enum, Float, ForeignKey, Integer,
                        String)
from sqlalchemy.orm import Mapped, relationship

from ..models.declarative_base import Base


class TypePaycodeEnum(str, enum.Enum):
    standard = 'standard'
    duration = 'duration'
    domino = 'domino'

class UnitPaycodeEnum(str, enum.Enum):
    hours = 'hours'
    money = 'money'
    days = 'days'

class AmountPaycodesHoursEnum(str, enum.Enum):
    none = 'none'
    productive = 'productive'
    no_productive = 'no_productive'


class VisiblesViewsOptionsGeneral(enum.IntFlag):
    visible_principal_area = 1
    visible_total_ficha = 2
    visible_params_reports = 4
    active_app_comment = 8


class OptionsGeneral(Base):
    __tablename__ = "options_general_r_paycode"

    paycode_id:                             Mapped[int] = Column(Integer, ForeignKey("paycode.paycode_id"), primary_key=True)
    _visibles_views:                        Mapped[int] = Column("visibles_views", Integer)
    time_and_attendance:                    Mapped[int] = Column(Integer)
    amount_paycodes_hours:                  Mapped[AmountPaycodesHoursEnum] = Column(Enum(AmountPaycodesHoursEnum))

    @property
    def visibles_views(self) -> list:
        ls = [v.name for v in VisiblesViewsOptionsGeneral if v & self._visibles_views]
        if len(ls) == 0:
            ls = []
        return ls

    @visibles_views.setter
    def visibles_views(self, value:list[VisiblesViewsOptionsGeneral]) -> None:
        self._visibles_views = 0
        for v in value:
            self._visibles_views |= v.value



class WeightedAverageCalculation(Base):
    __tablename__ = "weighted_average_calculation_r_paycode"

    paycode_id:                             Mapped[int] = Column(Integer, ForeignKey("paycode.paycode_id"), primary_key=True)
    visibles_views:                         Mapped[int] = Column("visibles_views", Integer)
    time_and_attendance:                    Mapped[int] = Column(Integer)
    amount_paycodes_hours:                  Mapped[AmountPaycodesHoursEnum] = Column(Enum(AmountPaycodesHoursEnum))

class Paycode(Base):
    __tablename__ = "paycode"

    paycode_id:                             Mapped[int] =              Column(Integer, primary_key=True, index=True)
    name:                                   Mapped[str] =              Column(String, unique=True)
    description:                            Mapped[str] =              Column(String)
    abbreviated_name:                       Mapped[str] =              Column(String)
    timetime_ip_aliases:                    Mapped[str] =              Column(String)
    code_number:                            Mapped[str] =              Column(String)
    type:                                   Mapped[TypePaycodeEnum] =  Column(Enum(TypePaycodeEnum))
    unit:                                   Mapped[UnitPaycodeEnum] =  Column(Enum(UnitPaycodeEnum), nullable=True)
    timesheet_resolved_exception:           Mapped[bool] =             Column(Boolean, nullable=True)
    requires_approval:                      Mapped[bool] =             Column(Boolean, nullable=True)
    unjustified_exception:                  Mapped[bool] =             Column(Boolean, nullable=True)
    justified_exception:                    Mapped[bool] =             Column(Boolean, nullable=True)
    asscociate_paycode:                     Mapped[bool] =             Column(Boolean, nullable=True)
    paycode_asociate:                       Mapped[int] =              Column(Integer, ForeignKey("paycode.paycode_id"), nullable=True)
    always_process_duration_separate_shift: Mapped[bool] =             Column(Boolean, nullable=True)
    multiplier:                             Mapped[float] =            Column(Float)
    add:                                    Mapped[float] =            Column(Float)
    enable:                                 Mapped[bool] =             Column(Boolean)

    options_general                         = relationship("OptionsGeneral", uselist=False, lazy="joined")
    weighted_average_calculation            = relationship("WeightedAverageCalculation", uselist=False, lazy="joined")
