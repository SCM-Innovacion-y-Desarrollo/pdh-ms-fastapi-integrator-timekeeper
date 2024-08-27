from datetime import time
from typing import Optional

from pydantic import BaseModel

from src.models.system import DaysIntEnum, DaysNameEnum
from src.models.zone import (DiferentialQualifiersBasedByEnum,
                             TypeConsecutiveEnum, TypeZoneEnum,
                             WeekDaysApplyToEnum)


class HolidaySelectedInput(BaseModel):
    holiday_id: Optional[int]
    holiday_extend_zone_rule: Optional[int]

class ZoneModelInput(BaseModel):
    #zone_id: Optional[int] = None
    name: str
    description: Optional[str] = None
    type: TypeZoneEnum
    requires_approval: bool

class HolidayInput(ZoneModelInput):
    defined_by: Optional[str]
    deducted_time: Optional[str]
    hours_worked_belong_to: Optional[str]
    #holidays: Optional[list[int]] = []

class WeekDaysInput(ZoneModelInput):
    days: Optional[list[DaysIntEnum]]
    applies_to: Optional[WeekDaysApplyToEnum]

class SustitutionOvertimeInput(BaseModel):
    overtime_rule_id: Optional[int]
    zone_id: Optional[int]

class ConsecutiveDaysWorkedInput(ZoneModelInput):
    day_amount: Optional[int]
    min_hours: Optional[time]
    min_hours_last_day: Optional[time]
    type_consecutive: Optional[TypeConsecutiveEnum]
    consecutive_days_numberday: Optional[int]
    consecutive_days_day_week: Optional[DaysNameEnum]
    days_week_restart_day: Optional[DaysNameEnum]

class DifferentialDailyInput(ZoneModelInput):
    start_hour: Optional[time]
    end_hour: Optional[time]
    min_hours_in_zone: Optional[time]
    min_hours_in_shift: Optional[time]
    margin_early: Optional[time]
    margin_late: Optional[time]
    planned: Optional[bool]
    based_by: Optional[DiferentialQualifiersBasedByEnum]
    start_work_before: Optional[time]
    start_work_after: Optional[time]
    end_work_before: Optional[time]
    end_work_after: Optional[time]

class DifferencialWeekendlyInput(ZoneModelInput):
    start_hour: Optional[time]
    end_hour: Optional[time]
    min_hours_in_zone: Optional[time]
    min_hours_in_shift: Optional[time]
    margin_early: Optional[time]
    margin_late: Optional[time]
    planned: Optional[bool]
    based_by: Optional[DiferentialQualifiersBasedByEnum]
    start_work_before: Optional[time]
    start_work_after: Optional[time]
    end_work_before: Optional[time]
    end_work_after: Optional[time]
    start_day: Optional[DaysNameEnum]
    end_day: Optional[DaysNameEnum]

class GeneralZoneModelInput(BaseModel):
    zone_id: Optional[int] = None
    name: Optional[str]
    description: Optional[str]
    type: Optional[TypeZoneEnum]
    requires_approval: Optional[bool]
    # Holiday
    defined_by: Optional[str] = None
    deducted_time: Optional[str] = None
    hours_worked_belong_to: Optional[str] = None
    selected_holidays: Optional[list[int]] = None
    # WeekDays
    days: Optional[list[DaysIntEnum]] = None
    applies_to: Optional[WeekDaysApplyToEnum] = None
    # ConsecutiveDaysWorked
    day_amount: Optional[int] = None
    min_hours: Optional[time] = None
    min_hours_last_day: Optional[time] = None
    type_consecutive: Optional[TypeConsecutiveEnum] = None
    consecutive_days_numberday: Optional[int] = None
    consecutive_days_day_week: Optional[DaysNameEnum] = None
    days_week_restart_day: Optional[DaysNameEnum] = None
    selected_sustitutions: Optional[list[int]] = None
    # DiferencialDaily && DifferencialWeekendly
    start_hour: Optional[time] = None
    end_hour: Optional[time] = None
    min_hours_in_zone: Optional[time] = None
    min_hours_in_shift: Optional[time] = None
    margin_early: Optional[time] = None
    margin_late: Optional[time] = None
    planned: Optional[bool] = None
    based_by: Optional[DiferentialQualifiersBasedByEnum] = None
    start_work_before: Optional[time] = None
    start_work_after: Optional[time] = None
    end_work_before: Optional[time] = None
    end_work_after: Optional[time] = None
    # DifferencialWeekendly
    start_day: Optional[DaysNameEnum] = None
    end_day: Optional[DaysNameEnum] = None