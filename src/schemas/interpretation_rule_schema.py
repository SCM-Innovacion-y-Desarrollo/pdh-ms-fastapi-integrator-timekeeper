from pydantic import BaseModel
from typing import List, Optional, Union
from src.models.interpretation_rule import InterpretationRule, PunchRestrictionEnum
from typing import List, Optional

from pydantic import BaseModel

from fastapi_filter.contrib.sqlalchemy.filter import Filter
from src.models.interpretation_rule import (InterpretationRule,
                                            PunchRestrictionEnum)
from src.models.system import BaseModelo
from src.schemas.filters import FilterModel


class InterpretationRuleModel(BaseModel):
    interpretation_rule_id:          int
    name:                            Optional[str]
    description:                     Optional[str]
    punch_restriction:               Optional[PunchRestrictionEnum]
    allow_substitution:              Optional[bool]
    early_start_margin:              Optional[str]
    early_start_restriction:         Optional[str]
    late_start_restriction:          Optional[str]
    late_start_margin:               Optional[str]
    omitted_output_margin:           Optional[str]
    brake_maximum_output :           Optional[str]
    brake_minimum_refreshment_ :     Optional[str]
    brake_impose_reset :             Optional[bool]
    brake_early_rest_start :         Optional[str]
    brake_late_rest_start_margin :   Optional[str]
    brake_late_rest_end_margin :     Optional[str]
    start_early_end_restriction :    Optional[str]
    end_early_end_restriction :      Optional[str]
    late_end_restriction :           Optional[str]
    punch_out_limit_omitted :        Optional[str]
    restrict_unplanned_punch_in:     Optional[bool]
    unplanned_shift_duration :       Optional[str]
    enable:                          Optional[bool]

class InterpreationPunchInputModel(BaseModel):
    name: Optional[str] = None
    description:                     Optional[str]                           = None
    punch_restriction:               Optional[PunchRestrictionEnum]
    allow_substitution:              Optional[bool]                          = None
    early_start_margin:              Optional[str]                           = None
    early_start_restriction:         Optional[str]                           = None
    late_start_restriction:          Optional[str]                           = None
    late_start_margin:               Optional[str]                           = None
    omitted_output_margin:           Optional[str]                           = None
    brake_maximum_output :           Optional[str]                           = None
    brake_minimum_refreshment_ :     Optional[str]                           = None
    brake_impose_reset :             Optional[bool]                          = None
    brake_early_rest_start :         Optional[str]                           = None
    brake_late_rest_start_margin :   Optional[str]                           = None
    brake_late_rest_end_margin :     Optional[str]                           = None
    start_early_end_restriction :    Optional[str]                           = None
    end_early_end_restriction :      Optional[str]                           = None
    late_end_restriction :           Optional[str]                           = None
    punch_out_limit_omitted :        Optional[str]                           = None
    restrict_unplanned_punch_in:     Optional[bool]                          = None
    unplanned_shift_duration :       Optional[str]                           = None
    enable:                          Optional[bool]                          = None

class InterpretationPunchRuleFilterModel(FilterModel):

    interpretation_rule_id__in: Optional[list[str]] = None

    order_by: List[str] = ["name"]
    search: Optional[str] = None

    class Constants(Filter.Constants):
        model = InterpretationRule
        search_model_fields = ["name", "enable"]


class InterpretationRuleModelDeleteInput(BaseModelo):
    interpretation_rule_ids: List[int]

class InterpretationRuleModelDeleteResponse(BaseModelo):
    count_deleted: int
    deleted: List[InterpretationRuleModel]


class InterprationByPayRule(BaseModel):
    data: Union[InterpretationRuleModel, str]