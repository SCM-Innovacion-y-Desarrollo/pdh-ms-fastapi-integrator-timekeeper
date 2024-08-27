from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import Mapped

from ..models.declarative_base import Base


class PunchMatch(Base):
    __tablename__ = "punch_match"

    punch_match_id:     Mapped[int] = Column(Integer, primary_key=True, index=True)
    in_punch:          Mapped[str] = Column(Integer, nullable=True)
    out_punch:          Mapped[str] = Column(Integer, nullable=True)
    scheduled_id:        Mapped[bool] = Column(Integer, nullable=True)
    start_reason:       Mapped[str] = Column(String)
    end_reason:         Mapped[str] = Column(String)
