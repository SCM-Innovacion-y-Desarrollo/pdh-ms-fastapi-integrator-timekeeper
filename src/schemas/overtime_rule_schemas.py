
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from fastapi_filter.contrib.sqlalchemy.filter import Filter
from ..models.overtime_rule import OvertimeRule, ValidityPeriodEnum
from ..models.system import DaysNameEnum
from ..schemas.filters import FilterModel
from ..schemas.paycode_schemas import PaycodeModel


class OvertimeRuleModel(BaseModel):
    """Overtime Rule Model"""
    name: str
    description: Optional[str]
    overtime_start: str
    validity_period: ValidityPeriodEnum
    restart_date: Optional[datetime]
    restart_week: Optional[DaysNameEnum]
    min_hour_calification: str
    required_approval: bool

class OvertimeRuleCreateModel(OvertimeRuleModel):
    """Overtime Rule Create Model"""
    paycodes: List[int] = []


class OvertimeRuleUpdateModel(OvertimeRuleModel):
    """Overtime Rule Update Model"""
    name: Optional[str] = None
    description: Optional[str] = None
    overtime_start: Optional[str] = None
    validity_period: Optional[ValidityPeriodEnum] = None
    restart_date: Optional[datetime] = None
    restart_week: Optional[DaysNameEnum] = None
    min_hour_calification: Optional[str] = None
    required_approval: Optional[bool] = None
    paycodes: Optional[List[int]] = []

class OvertimeRuleIDModel(OvertimeRuleModel):
    overtime_rule_id: int
    id:  int


class OvertimeRuleDBModel(OvertimeRuleIDModel):
    """Overtime Rule DB Model"""
    enable: bool
    paycodes: Optional[List[PaycodeModel]]

class OvertimeRuleModelFilter(FilterModel):
    """Overtime Rule Model Filter"""
    overtime_rule_id: Optional[int] = None

    name: Optional[str] = None
    name__ilike: Optional[str] = None
    name__like: Optional[str] = None
    name__neq: Optional[str] = None

    order_by: List[str] = ["name"]
    search: Optional[str] = None

    class Constants(Filter.Constants):
        model = OvertimeRule
        search_model_fields = ["name"]
