
from typing import Optional, List
from typing import List, Optional

from src.models.system import BaseModelo, DaysNameEnum
from src.schemas.holiday_schemas import HolidayModel
from src.models.system import BaseModelo, DaysNameEnum
from src.models.pay_rule import PayRule
from fastapi_filter.contrib.sqlalchemy.filter import Filter



class PayRuleRWorkRuleModel(BaseModelo):
    work_rule_id:    int
    start_hour:      str
    end_hour:        str
    min_shift:       str
    max_shift:       str
    days_week:       List[DaysNameEnum]
    planned:         bool
    unplanned:       bool
    order:           int

class PayRuleRWorkRuleDBModel(PayRuleRWorkRuleModel):
    pay_rule_r_work_rule_id: int
    pay_rule_id:     int

class PayRuleRWorkRuleUpdateModel(PayRuleRWorkRuleDBModel):
    pay_rule_r_work_rule_id: Optional[int] = None
    pay_rule_id:     Optional[int] = None

class PayRuleRWorkRuleCreateModel(PayRuleRWorkRuleModel):
    pass

class PayRuleModel(BaseModelo):
    name: Optional[str]
    description: Optional[str]
    interpretation_rule_id: Optional[int]
    credit_holiday_default_id: Optional[int]
    fixed_rule_id: Optional[int]
    work_rule_default_id: Optional[int]
    calculate_projected_totals: Optional[bool]
    treat_planned_hour: Optional[bool]

class PayRuleCreateModel(PayRuleModel):
    asignation: List[PayRuleRWorkRuleModel]
    holidays: List[int]
    enable: Optional[bool] = None

class PayRuleUpdateModel(PayRuleModel):
    pay_rule_id: int
    asignation: List[PayRuleRWorkRuleUpdateModel]
    holidays: List[int]

class PayRuleDBModel(PayRuleModel):
    pay_rule_id: int
    holidays: List[HolidayModel]
    asignation: List[PayRuleRWorkRuleDBModel]

    fixed_rule_name: Optional[str]
    work_rule_default_name: Optional[str]

class PayruleFilterModel(Filter):
    pay_rule_id__in: Optional[List[int]] = None
    name__contains: Optional[str] = None
    description__contains: Optional[str] = None
    interpretation_rule_id__in: Optional[int] = None
    credit_holiday_default_id__in: Optional[int] = None
    fixed_rule_id__in: Optional[int] = None
    work_rule_default_id__in: Optional[int] = None
    calculate_projected_totals__eq: Optional[bool] = None
    treat_planned_hour__eq: Optional[bool] = None
    enable__eq: Optional[bool] = None
    holidays__in: Optional[int] = None
    asignation__in: Optional[int] = None
    order_by: List[str] = ["name"]

    class Constants(Filter.Constants):
        model = PayRule
        search_model_fields = ["enable"]


