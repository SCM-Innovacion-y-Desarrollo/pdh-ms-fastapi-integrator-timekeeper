from typing import Dict, List, Optional, Union

from pydantic import BaseModel

from fastapi_filter.contrib.sqlalchemy.filter import Filter
from src.models.paycode import (AmountPaycodesHoursEnum, Paycode,
                                TypePaycodeEnum, UnitPaycodeEnum)
from src.models.system import BaseModelo
from src.schemas.filters import FilterModel


class OptionsGeneralModel(BaseModelo):
    paycode_id: int
    visibles_views: List[str]
    time_and_attendance: int
    amount_paycodes_hours: AmountPaycodesHoursEnum


class WeightedAverageCalculation(OptionsGeneralModel):
    pass

class PaycodeModel(BaseModelo):
    paycode_id: Optional[int] = None
    name: str
    description: Optional[str] = None
    abbreviated_name: Optional[str] = None
    timetime_ip_aliases: Optional[str] = None
    code_number: Optional[str] = None
    type: TypePaycodeEnum
    unit: UnitPaycodeEnum
    timesheet_resolved_exception: Optional[bool] = None
    requires_approval: Optional[bool] = None
    unjustified_exception: Optional[bool] = None
    justified_exception:Optional[ bool] = None
    asscociate_paycode: Optional[bool] = None
    paycode_asociate: Optional[int] = None
    always_process_duration_separate_shift: Optional[bool] = None
    multiplier: Optional[float] = None
    add:    Optional[float] = None
    enable: Optional[bool] = None

    options_general: Optional[OptionsGeneralModel] = None
    weighted_average_calculation: Optional[WeightedAverageCalculation] = None


class ListPaycodeModel(BaseModel):
    data: List[PaycodeModel]

class PaycodeModelInput(BaseModelo):
    paycode_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    abbreviated_name: Optional[str] = None
    timetime_ip_aliases: Optional[str] = None
    code_number: Optional[str] = None
    type: Optional[TypePaycodeEnum] = None
    unit: Optional[UnitPaycodeEnum] = None
    timesheet_resolved_exception: Optional[bool] = None
    requires_approval: Optional[bool] = None
    unjustified_exception: Optional[bool] = None
    justified_exception:Optional[ bool] = None
    asscociate_paycode: Optional[bool] = None
    paycode_asociate: Optional[int] = None
    always_process_duration_separate_shift: Optional[bool] = None
    multiplier: Optional[float] = None
    add:    Optional[float] = None
    enable: Optional[bool] = None

    options_general: Optional[OptionsGeneralModel] = None
    weighted_average_calculation: Optional[WeightedAverageCalculation] = None


class PaycodesFilterModel(FilterModel):

    paycode_id: Optional[list[str]] = None
    paycode_id__in: Optional[list[str]] = None

    name : Optional[str] = None
    name__ilike: Optional[str] = None
    name__like: Optional[str] = None
    name__neq: Optional[str] = None

    description__ilike: Optional[str] = None
    description__like: Optional[str] = None
    description__neq: Optional[str] = None

    type: Optional[str] = None

    order_by: Optional[List[str]] = None
    search: Optional[Dict[str, Union[str, int]]] = None

    active: Optional[bool] = None

    class Constants(Filter.Constants):
        model = Paycode
        search_model_fields = ["name", "enable"]