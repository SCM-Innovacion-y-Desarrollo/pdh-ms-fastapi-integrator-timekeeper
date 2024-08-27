from datetime import date, time
from typing import List, Optional

from pydantic import BaseModel

from fastapi_filter.contrib.sqlalchemy.filter import Filter
from ..models.fixed_rule import (FixedRule, HoursBelongToEnum,
                                   TypePaymentPeriodEnum)
from ..schemas.filters import FilterModel


class FixedRuleModel(BaseModel):
    fixed_rule_id: int
    name: Optional[str]
    type_payment_period: Optional[TypePaymentPeriodEnum]
    date_reference: Optional[date]
    days: Optional[int]
    day_reference: Optional[int]
    day_division_hours: Optional[time]
    hours_belong_to: Optional[HoursBelongToEnum]
    enable: Optional[bool]

class FixedRuleInputModel(BaseModel):
    name: Optional[str] = None
    type_payment_period: Optional[TypePaymentPeriodEnum] = None
    date_reference: Optional[date] = None
    days: Optional[int] = None
    day_reference:  Optional[int] = None
    day_division_hours: Optional[time] = None
    hours_belong_to: Optional[HoursBelongToEnum] = None
    enable: Optional[bool] = None
    description: Optional[str] = None

class FixedRuleFilterModel(FilterModel):

    fixed_rule_id__in: Optional[list[str]] = None

    order_by: List[str] = ["name"]
    search: Optional[str] = None

    class Constants(Filter.Constants):
        model = FixedRule
        search_model_fields = ["name", "enable"]

class FixedRuleModelDeleteInput(BaseModel):
    fixed_rule_ids: List[int]

class FixedRuleModelDeleteResponse(BaseModel):
    count_deleted: int
    deleted: List[FixedRuleModel]