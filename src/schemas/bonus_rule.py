from datetime import time
from typing import Optional

from pydantic import BaseModel

from ..models.bonus_rule import BonusActivateByEnum, TimePeriodEnum
from ..models.system import DaysNameEnum


class BonusRuleInput(BaseModel):
    bonus_rule_id:              Optional[int]                 = None
    name:                       Optional[str]                 = None
    description:                Optional[str]                 = None
    amount:                     Optional[time]                = None
    days_in_week:               Optional[list[int]]           = None
    is_exception:               Optional[bool]                = None
    paycode_id:                 Optional[int]                 = None
    break_id:                   Optional[int]                 = None
    allow_cancel_in_timesheet:  Optional[bool]                = None
    use_shift_restriction:      Optional[bool]                = None
    start_shift_restriction:    Optional[time]                = None
    end_shift_restriction:      Optional[time]                = None
    activate_by:                Optional[BonusActivateByEnum] = None

class ActivateByPaycodeInput(BonusRuleInput):
    #bonus_rule_id:      Optional[int]             = None
    active_paycode_id:               Optional[int]             = None
    minimum:                         Optional[time]            = None
    maximum:                         Optional[time]            = None
    time_period:                     Optional[TimePeriodEnum]  = None
    achieve_requirements_for_shift:  Optional[bool]            = None
    shifts_required:                 Optional[int]             = None
    start_day_week:                  Optional[DaysNameEnum]    = None

class ShiftDurationInput(BonusRuleInput):
    #bonus_rule_id:                        Optional[int]  = None
    use_limit_hour_shift_round:           Optional[bool] = None
    exception_short_break_unqualif_break: Optional[bool] = None
    min_interval_qualif:                  Optional[time] = None
    min_duration_shift_to_activate:       Optional[time] = None
    max_duration_shift_to_activate:       Optional[time] = None
    location:                             Optional[time] = None
    activate_if_location_match_or_after:  Optional[time] = None
    activate_if_location_is_befora:       Optional[time] = None

class HourDayInput(BonusRuleInput):
    #bonus_rule_id:  Optional[int]  = None
    hour:           Optional[time] = None

class BonusRuleGeneralInput(BaseModel):
    #bonus_rule_id:              Optional[int]                 = None
    name:                       Optional[str]                 = None
    description:                Optional[str]                 = None
    amount:                     Optional[time]                = None
    days_in_week:               Optional[list[int]]           = None
    is_exception:               Optional[bool]                = None
    paycode_id:                 Optional[int]                 = None
    break_id:                   Optional[int]                 = None
    allow_cancel_in_timesheet:  Optional[bool]                = None
    use_shift_restriction:      Optional[bool]                = None
    start_shift_restriction:    Optional[time]                = None
    end_shift_restriction:      Optional[time]                = None
    activate_by:                Optional[BonusActivateByEnum] = None
    # ActiveByPaycode
    active_paycode_id:                Optional[int]             = None
    minimum:                          Optional[time]            = None
    maximum:                          Optional[time]            = None
    time_period:                      Optional[TimePeriodEnum]  = None
    achieve_requirements_for_shifts:  Optional[bool]            = None
    shifts_required:                  Optional[int]             = None
    start_day_week:                   Optional[DaysNameEnum]    = None
    # ShiftDuration
    use_limit_hour_shift_round:           Optional[bool]      = None
    exception_short_break_unqualif_break: Optional[bool]      = None
    min_interval_qualif:                  Optional[time]      = None
    min_duration_shift_to_activate:       Optional[time]      = None
    max_duration_shift_to_activate:       Optional[time]      = None
    location:                             Optional[time]      = None
    activate_if_location_match_or_after:  Optional[time]      = None
    activate_if_location_is_befora:       Optional[time]      = None
    # HourDay
    hour:                                 Optional[time]      = None