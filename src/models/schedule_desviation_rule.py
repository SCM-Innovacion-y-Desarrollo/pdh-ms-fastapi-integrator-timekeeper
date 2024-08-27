from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import Mapped

from ..models.declarative_base import Base


class ScheduleDesviationRule(Base):
    __tablename__ = "schedule_desviation_rule"

    schedule_desviation_rule_id:    Mapped[int] =    Column(Integer, primary_key=True, index=True)
    name:                           Mapped[str] =    Column(String, unique=True)
    description:                    Mapped[str] =    Column(String)
    before_shift:                   Mapped[bool] =   Column(Boolean)
    after_shift:                    Mapped[bool] =   Column(Boolean)
    requires_approval:              Mapped[bool] =   Column(Boolean)
    unplanned:                      Mapped[bool] =   Column(Boolean)
    enable:                         Mapped[bool] =   Column(Boolean)

    @property
    def id(self) -> int:
        return self.schedule_desviation_rule_id