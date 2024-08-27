from datetime import date, time
from typing import Generic, List, Optional, TypeVar
from pydantic import BaseModel


from ..models.break_rule import StartBreakByEnum
from ..models.rounding_rule import TypePunchOmitedRoundingEnum
from ..models.bonus_rule import TimePeriodEnum
from ..models.fixed_rule import HoursBelongToEnum, TypePaymentPeriodEnum
from ..models.zone import (
    TypeConsecutiveEnum,
    DiferentialQualifiersBasedByEnum, TypeZoneEnum,
    DaysNameEnum, HolidayZoneDeductedTimeEnum,
    HolidayZoneDefinedByEnum, HolidayZoneHoursWorkedBelongToEnum,
    WeekDaysApplyToEnum
)


from ..schemas.holiday_schemas import HolidayModel
from ..schemas.overtime_rule_schemas import OvertimeRuleDBModel

from ..models.system import BaseModelo

M = TypeVar("M", bound=BaseModel)
T = TypeVar('T', bound=BaseModel)

class ResponseModel(BaseModel, Generic[M]):
    status: Optional[str] = "success"
    data: List[M] | M

class InputModel(BaseModel, Generic[T]):
    data: T

class ZoneModel(BaseModelo):
    zone_id: int
    name: str
    description: str
    type: TypeZoneEnum
    requires_approval: bool
    id: int

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

class WeekDaysModel(ZoneModel):
    days: Optional[List[str]]
    applies_to: WeekDaysApplyToEnum

class DiferentialDailyModel(ZoneModel):
    start_hour:         Optional[time]
    end_hour:           Optional[time]
    min_hours_in_zone:  Optional[time]
    min_hours_in_shift: Optional[time]
    margin_early:       Optional[time]
    margin_late:        Optional[time]
    planned:            Optional[bool]
    based_by:           Optional[DiferentialQualifiersBasedByEnum]
    start_work_before:  Optional[time]
    start_work_after:   Optional[time]
    end_work_before:    Optional[time]
    end_work_after:     Optional[time]

class DiferentialWeekendlyModel(DiferentialDailyModel):
    start_day:  Optional[DaysNameEnum]
    end_day:    Optional[DaysNameEnum]



class ZoneHolidayModel(ZoneModel):
    defined_by: HolidayZoneDefinedByEnum
    deducted_time: HolidayZoneDeductedTimeEnum
    hours_worked_belong_to: HolidayZoneHoursWorkedBelongToEnum

    holidays: List["HolidayModel"]

class ConsecutiveDaysWorkedZoneModel(ZoneModel):
    day_amount: int
    min_hours: time
    min_hours_last_day: time
    type_consecutive: TypeConsecutiveEnum
    consecutive_days_numberday: int
    consecutive_days_day_week: Optional[DaysNameEnum]
    days_week_restart_day: Optional[DaysNameEnum]

    sustitution_overtime: Optional[List["OvertimeRuleDBModel"]]


class HolidayZoneModel(ZoneModel):
    defined_by: Optional[HolidayZoneDefinedByEnum]
    deducted_time: Optional[HolidayZoneDeductedTimeEnum]
    hours_worked_belong_to: Optional[HolidayZoneHoursWorkedBelongToEnum]
    holidays: List["HolidayModel"]



class ListZoneModel(BaseModel):
    data: List[HolidayZoneModel]
    # data: List[HolidayZoneModel | ConsecutiveDaysWorkedZoneModel]

class ScheduleDesviationRuleModel(BaseModel):
    schedule_desviation_rule_id: int
    name: str
    description: Optional[str]
    before_shift: bool
    after_shift: bool
    requires_approval: bool
    unplanned: bool
    enable: bool
    id: int

class RoundingConfigPunchRRoundingRuleModel(BaseModel):
    rounding_rule_id: int
    in_out: bool
    early_late: bool
    change_point: Optional[time]
    rounding_extern: Optional[time]
    rounding_intern: Optional[time]
    grace_period_extern: Optional[time]
    grace_period_intern: Optional[time]

class RoundingConfigUnplanRRoundingRuleModel(BaseModel):
    rounding_rule_id: int
    rounding_entry: Optional[time]
    grace_period_entry: Optional[time]
    rounding_exit: Optional[time]
    grace_period_exit: Optional[time]
    rounding_trans: Optional[time]
    grace_period_trans: Optional[time]

class RoundingConfigPunchOmitedRRoundingRuleModel(BaseModel):
    rounding_rule_id: int
    planified: bool
    type: Optional[TypePunchOmitedRoundingEnum]
    is_exception: Optional[bool]


class RoundingRuleModel(BaseModelo):
    rounding_rule_id: int
    name: str
    description: Optional[str]

    config_punch_r_rounding_rule: Optional[List[RoundingConfigPunchRRoundingRuleModel]]
    rounding_config_unplan_r_rounding_rule: Optional[RoundingConfigUnplanRRoundingRuleModel]
    rounding_config_punch_omited_r_rounding_rule: Optional[RoundingConfigPunchOmitedRRoundingRuleModel]


class ListRoundingRuleModel(BaseModel):
    data: List[RoundingRuleModel]




class ExceptionRuleModel(BaseModel):
    exception_rule_id: int
    name: Optional[str]
    description: Optional[str]
    not_planning: Optional[bool]
    long_interval: Optional[time]
    shortened_shift: Optional[time]
    in_punch_very_early: Optional[time]
    in_punch_early: Optional[time]
    in_punch_late: Optional[time]
    out_punch_early: Optional[time]
    out_punch_late: Optional[time]
    out_punch_very_late: Optional[time]
    in_paycode_id: Optional[int]
    out_paycode_id: Optional[int]


class CombinationRuleModel(BaseModelo):
    combination_rule_id: int
    name: str
    description: str
    default: bool

    overtime_rules:              Optional[List[OvertimeRuleDBModel]] = []
    zones:                       Optional[List[ZoneModel]] = []
    schedule_desviation_rules:   Optional[List[ScheduleDesviationRuleModel]] = []


class CombinationRuleModelInput(BaseModelo):
    name: Optional[str] = None
    description: Optional[str] = None
    default: Optional[bool] = None

    overtime_rules:              Optional[List[OvertimeRuleDBModel]] = None
    zones:                       Optional[List[ZoneModel]] = None
    schedule_desviation_rules:   Optional[List[ScheduleDesviationRuleModel]] = None



class ListCombinationRuleModel(BaseModel):
    data: List[CombinationRuleModel]


class CombinationRuleNameModel(BaseModel):
    name: str


class BreakRuleModel(BaseModelo):
    name: Optional[str]
    duration_normal: Optional[time]
    duration_medio: Optional[time]
    duration_max: Optional[time]
    use_rounding_punch_unplan: Optional[bool]
    break_short_round: Optional[time]
    break_short_grace_period: Optional[time]
    break_intermedio_round: Optional[time]
    break_intermedio_grace_period: Optional[time]
    break_long_round: Optional[time]
    break_long_grace_period: Optional[time]
    start_break_after: Optional[time]
    start_break_before: Optional[time]
    start_break_by: Optional[StartBreakByEnum]
    start_break_amount_pay: Optional[time]
    start_break_limit_except_short: Optional[time]
    start_break_limit_except_long: Optional[time]
    enable: bool = True

class BreakRuleModelUpdate(BaseModelo):
    name: Optional[str] = None
    duration_normal: Optional[time] = None
    duration_medio: Optional[time] = None
    duration_max: Optional[time] = None
    use_rounding_punch_unplan: Optional[bool] = None
    break_short_round: Optional[time] = None
    break_short_grace_period: Optional[time] = None
    break_intermedio_round: Optional[time] = None
    break_intermedio_grace_period: Optional[time] = None
    break_long_round: Optional[time] = None
    break_long_grace_period: Optional[time] = None
    start_break_after: Optional[time] = None
    start_break_before: Optional[time] = None
    start_break_by: Optional[StartBreakByEnum] = None
    start_break_amount_pay: Optional[time] = None
    start_break_limit_except_short: Optional[time] = None
    start_break_limit_except_long: Optional[time] = None

class BreakRuleDBModel(BreakRuleModel):
    break_rule_id: int


class ListBreakRuleModel(BaseModel):
    data: List[BreakRuleDBModel]

class BonusRuleModel(BaseModelo):
    bonus_rule_id: int
    name: Optional[str]
    description: Optional[str]
    amount: Optional[time]
    days_in_week: Optional[List[str]]
    is_exception: Optional[bool]
    paycode_id: Optional[int]
    break_id: Optional[int]
    allow_cancel_in_timesheet: Optional[bool]
    use_shift_restriction: Optional[bool]
    start_shift_restriction: Optional[time]
    end_shift_restriction: Optional[time]
    activate_by: Optional[str]


class HourDayExtendBonusRuleModel(BonusRuleModel):
    hour: Optional[time]

class ShiftDurationExtendBonusRuleModel(BonusRuleModel):
    use_limit_hour_shift_round:             Optional[bool]
    exception_short_break_unqualif_break:   Optional[bool]
    min_interval_qualif:                    Optional[time]
    min_duration_shift_to_activate:         Optional[time]
    max_duration_shift_to_activate:         Optional[time]
    location:                               Optional[time]
    activate_if_location_match_or_after:    Optional[time]
    activate_if_location_is_befora:         Optional[time]

class ActiveByPaycodeExtendBonusRuleModel(BonusRuleModel):
    active_paycode_id:              Optional[int]
    minimum:                        Optional[time]
    maximum:                        Optional[time]
    time_period:                    Optional[TimePeriodEnum]
    achieve_requirements_for_shift: Optional[bool]
    shifts_required:                Optional[int]
    start_day_week:                 Optional[DaysNameEnum]

class ListBonusRuleModel(BaseModel):
    data: List[BonusRuleModel]

class WorkRuleModel(BaseModelo):
    work_rule_id: int
    name: str
    description: Optional[str]
    excepcion_rule_id: Optional[int]
    paycodes_distribution_id: Optional[int]
    rounding_rule_id: Optional[int]

    exception_rule_name: Optional[str]
    paycodes_distribution_name: Optional[str]
    rounding_rule_name: Optional[str]

    bonus:                       Optional[List[BonusRuleModel]]
    break_rules:                 Optional[List[BreakRuleDBModel]]
    overtime_rules:              Optional[List[OvertimeRuleDBModel]]
    zones:                       Optional[List[ZoneModel]]
    schedule_desviation_rules:   Optional[List[ScheduleDesviationRuleModel]]

class TokenData(BaseModel):
    username: str | None = None
    scopes: List[str] = []


class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    username: str
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str
    type: str | None = None