from typing import List, Optional

from pydantic import BaseModel

from fastapi_filter.contrib.sqlalchemy.filter import Filter
from ..models.credit_holiday_rule import (ConsiderOnExtratimeEnum,
                                            CreditHolidayRule, CreditTypeEnum,
                                            HoursBelongEnum,
                                            PayCreditsLikeEnum,
                                            PlannedMoreShiftEnum,
                                            ShiftEquivalentToEnum,
                                            TimeDeductedFromHolidayCredit,
                                            ZoneHolidayDefinedByEnum)
from ..models.system import BaseModelo
from ..schemas.filters import FilterModel
from ..schemas.paycode_schemas import PaycodeModel, PaycodeModelInput


class CreditHolidayRuleModel(BaseModel):
    holiday_rule_id:                            int
    name:                                       Optional[str]
    description:                                Optional[str]
    must_work_shift_before_holiday:             Optional[bool]
    must_work_shift_after_holiday:              Optional[bool]
    must_work_shift_before_or_after_holiday:    Optional[bool]
    must_work_shift_in_holiday:                 Optional[bool]
    amount_hours:                               Optional[str]
    shift_equivalent_to:                        Optional[ShiftEquivalentToEnum]
    credit_type:                                Optional[CreditTypeEnum]
    if_planned_more_one_shift_in_day:           Optional[PlannedMoreShiftEnum]
    hours_belong:                               Optional[HoursBelongEnum]
    zone_holiday_defined_by:                    Optional[ZoneHolidayDefinedByEnum]
    pay_credits_like:                           Optional[PayCreditsLikeEnum]
    work_rule_id:                               Optional[int]
    consider_on_extratime_limit:                Optional[ConsiderOnExtratimeEnum]
    consider_on_extratime_consecutive_days:     Optional[ConsiderOnExtratimeEnum]
    paycode_extratime_limit_id:                 Optional[int]
    paycode_extratime_consecutive_days_id:      Optional[int]
    enable:                                     Optional[bool]
    time_deducted_from_holiday_credit:          Optional[TimeDeductedFromHolidayCredit]

    paycode_extratime_limit:                    Optional[PaycodeModel]
    paycode_extratime_consecutive_days:         Optional[PaycodeModel]

    paycodes:                                   Optional[List[PaycodeModel]]

class CreditHolidayRuleInputModel(BaseModel):
    name:                                       Optional[str] = None
    description:                                Optional[str] = None
    must_work_shift_before_holiday:             Optional[bool] = None
    must_work_shift_after_holiday:              Optional[bool] = None
    must_work_shift_before_or_after_holiday:    Optional[bool] = None
    must_work_shift_in_holiday:                 Optional[bool] = None
    amount_hours:                               Optional[str] = None
    shift_equivalent_to:                        Optional[ShiftEquivalentToEnum] = None
    credit_type:                                Optional[CreditTypeEnum] = None
    if_planned_more_one_shift_in_day:           Optional[PlannedMoreShiftEnum] = None
    hours_belong:                               Optional[HoursBelongEnum]  = None
    zone_holiday_defined_by:                    Optional[ZoneHolidayDefinedByEnum] = None
    pay_credits_like:                           Optional[PayCreditsLikeEnum] = None
    work_rule_id:                               Optional[int] = None
    consider_on_extratime_limit:                Optional[ConsiderOnExtratimeEnum] = None
    consider_on_extratime_consecutive_days:     Optional[ConsiderOnExtratimeEnum] = None
    paycode_extratime_limit_id:                 Optional[int] = None
    paycode_extratime_consecutive_days_id:      Optional[int] = None
    paycode_list:                               Optional[List[PaycodeModelInput]] = None
    enable:                                     Optional[bool] = None
    time_deducted_from_holiday_credit:          Optional[TimeDeductedFromHolidayCredit] = None

class CreditHolidayRuleFilterModel(FilterModel):

    holiday_rule_id__in: Optional[list[str]] = None

    order_by: List[str] = ["name"]
    search: Optional[str] = None

    class Constants(Filter.Constants):
        model = CreditHolidayRule
        search_model_fields = ["name", "enable"]

class WorkRuleMinimalModel(BaseModelo):
    work_rule_id: int
    name: str

class PaycodesMinimalModel(BaseModelo):
    paycode_id: int
    name: str
    type: str

class CreditHolidayRuleModelDeleteInput(BaseModelo):
    credit_holiday_rule_ids: List[int]

class CreditHolidayRuleModelDeleteResponse(BaseModelo):
    count_deleted: int
    deleted: List[CreditHolidayRuleModel]
