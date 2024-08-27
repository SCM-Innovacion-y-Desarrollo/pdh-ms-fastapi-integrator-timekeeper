from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship

from ..models.declarative_base import Base


class PaycodeCombination(Base):
    __tablename__ = "paycode_combination"

    paycode_combination_id:  Mapped[int]        = Column(Integer, primary_key=True, index=True)
    name:                    Mapped[str]        = Column(String, unique=True)
    description:             Mapped[str]        = Column(String)
    start_date:              Mapped[datetime]   = Column(DateTime)
    end_date:                Mapped[datetime]   = Column(DateTime)
    enable:                  Mapped[bool]       = Column(Boolean)


    paycodes = relationship("Paycode", secondary="paycode_combination_r_paycode", lazy="joined", viewonly=True)
    combinations = relationship("PaycodeCombinationRPaycode", lazy="joined", viewonly=True)



class PaycodeCombinationRPaycode(Base):
    __tablename__ = "paycode_combination_r_paycode"

    paycode_id: Mapped[int] = Column(Integer, ForeignKey("paycode.paycode_id"), primary_key=True)
    paycode_combination_id: Mapped[int] = Column(Integer, ForeignKey("paycode_combination.paycode_combination_id"), primary_key=True)
    start_date: Mapped[datetime] = Column(DateTime)
    end_date: Mapped[datetime] = Column(DateTime)

    paycode = relationship("Paycode", foreign_keys=[paycode_id])