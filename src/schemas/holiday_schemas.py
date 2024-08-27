
from datetime import datetime
from typing import List, Optional

from iso3166 import countries
from pydantic import validator

from fastapi_filter.contrib.sqlalchemy.filter import Filter
from src.models.holiday import Holiday
from src.models.system import BaseModelo
from src.schemas.filters import FilterModel


class CountryModel(BaseModelo):
    country: str

    @validator("country")
    def country_must_valid(cls, v):
        if v:
            try:
                contry = countries.get(v).name
            except:
                raise ValueError('Country not exists')
        return v

class HolidayCreateModel(CountryModel):
    name: str
    public_name: str
    year: int
    country: str
    is_renounceable: bool
    is_local: bool
    start: datetime
    end: datetime

class HolidayModel(BaseModelo):
    holiday_id: Optional[int] = None
    name: Optional[str] = None
    public_name: Optional[str] = None
    year: Optional[int] = None
    country: Optional[str] = None
    is_renounceable: Optional[bool] = None
    is_local: Optional[bool] = None
    start: Optional[datetime] = None
    end: Optional[datetime] = None

class HolidayDBModel(HolidayModel):
    holiday_id: int
    enable: bool

class HolidayModelFilter(FilterModel):

    holiday_id: Optional[int] = None

    name: Optional[str] = None
    name__ilike: Optional[str] = None
    name__like: Optional[str] = None
    name__neq: Optional[str] = None

    public_name: Optional[str] = None
    public_name__ilike: Optional[str] = None
    public_name__like: Optional[str] = None
    public_name__neq: Optional[str] = None


    year: Optional[int] = None
    year__lt: Optional[int] = None
    year__lte: Optional[int] = None
    year__gt: Optional[int] = None
    year__gte: Optional[int] = None

    country: Optional[str] = None
    country__ilike: Optional[str] = None
    country__like: Optional[str] = None
    country__neq: Optional[str] = None

    is_renounceable: Optional[bool] = None
    is_local: Optional[bool] = None


    start: Optional[datetime] = None
    start__lt: Optional[datetime] = None
    start__lte: Optional[datetime] = None
    start__gt: Optional[datetime] = None
    start__gte: Optional[datetime] = None


    end: Optional[datetime] = None
    end__lt: Optional[datetime] = None
    end__lte: Optional[datetime] = None
    end__gt: Optional[datetime] = None
    end__gte: Optional[datetime] = None

    order_by: List[str] = ["name"]
    search: Optional[str] = None

    class Constants(Filter.Constants):
        model = Holiday
        search_model_fields = ["name", "public_name"]


