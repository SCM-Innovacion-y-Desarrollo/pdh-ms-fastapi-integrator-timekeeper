from typing import List, Optional

from pydantic import BaseModel

from fastapi_filter.contrib.sqlalchemy.filter import Filter
from src.models.schedule_desviation_rule import ScheduleDesviationRule
from src.models.system import BaseModelo
from src.schemas.filters import FilterModel


class ScheduleDesviationRuleModel(BaseModel):
    schedule_desviation_rule_id: int
    name: str
    description: Optional[str]
    before_shift: bool
    after_shift: bool
    requires_approval: bool
    unplanned: bool
    enable: bool

class ScheduleDesviationRuleModelInput(BaseModelo):
    name: Optional[str] = None
    description: Optional[str] = None
    before_shift: Optional[bool] = None
    after_shift: Optional[bool] = None
    requires_approval: Optional[bool] = None
    unplanned: Optional[bool] = None
    enable: Optional[bool] = None



class ScheduleDesviationRuleModelDeleteInput(BaseModelo):
    schedule_desviation_rule_ids: List[int]


class ScheduleDesviationRuleModelDeleteResponse(BaseModelo):
    count_deleted: int
    deleted: List[ScheduleDesviationRuleModel]


class ScheduleDesviationModelFilter(FilterModel):

    schedule_desviation_rule_id__in: Optional[list[str]] = None

    order_by: List[str] = ["name"]
    search: Optional[str] = None

    class Constants(Filter.Constants):
        model = ScheduleDesviationRule
        search_model_fields = ["name", "enable"]