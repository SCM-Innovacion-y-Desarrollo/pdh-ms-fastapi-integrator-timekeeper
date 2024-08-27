from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Time
from sqlalchemy.orm import Mapped, relationship

from ..models.declarative_base import Base


class ExceptionRule(Base):
    __tablename__ = "exception_rule"

    exception_rule_id:    Mapped[int] =    Column(Integer, primary_key=True, index=True)
    name:                 Mapped[str] =    Column(String)
    description:          Mapped[str] =    Column(String)
    not_planning:         Mapped[bool] =   Column(Boolean)
    long_interval:        Mapped[Time] =   Column(String)
    shortened_shift:      Mapped[Time] =   Column(String)
    in_punch_very_early:  Mapped[Time] =   Column(String)
    in_punch_early:       Mapped[Time] =   Column(String)
    in_punch_late:        Mapped[Time] =   Column(String)
    out_punch_early:      Mapped[Time] =   Column(String)
    out_punch_late:       Mapped[Time] =   Column(String)
    out_punch_very_late:  Mapped[Time] =   Column(String)
    in_paycode_id:        Mapped[int] =    Column(Integer, ForeignKey('paycode.paycode_id'), nullable=False)
    out_paycode_id:       Mapped[int] =    Column(Integer, ForeignKey('paycode.paycode_id'), nullable=False)
    enable:               Mapped[bool] =   Column(Boolean, default=True)

    in_paycode:           Mapped["Paycode"] =    relationship("Paycode", foreign_keys=[in_paycode_id], overlaps="paycodes", viewonly=True)
    out_paycode:          Mapped["Paycode"] =    relationship("Paycode", foreign_keys=[in_paycode_id], overlaps="paycodes")