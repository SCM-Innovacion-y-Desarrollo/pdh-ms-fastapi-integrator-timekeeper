from datetime import datetime

from iso3166 import countries
from sqlalchemy import Boolean, Column, DateTime, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, validates

from ..models.declarative_base import Base
from ..databases import Schema


class Holiday(Base, Schema):
    __tablename__ = "holiday"

    holiday_id:       Mapped[int] =        Column(Integer, primary_key=True, index=True)
    name:             Mapped[str] =        Column(String)
    public_name:      Mapped[str] =        Column(String)
    year:             Mapped[int] =        Column(SmallInteger)
    country:          Mapped[str] =        Column(String)
    is_renounceable:  Mapped[bool] =       Column(Boolean)
    is_local:         Mapped[bool] =       Column(Boolean)
    start:            Mapped[datetime] =   Column(DateTime)
    end:              Mapped[datetime] =   Column(DateTime)
    enable:           Mapped[bool] =       Column(Boolean, default=True)

    @validates('country')
    def validate_country(self, key, value):
        if value:
            contry = countries.get(value).name
        return value