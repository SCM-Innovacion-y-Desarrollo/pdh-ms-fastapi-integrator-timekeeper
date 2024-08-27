from typing import List, Optional

from pydantic.fields import Field

from fastapi_filter.contrib.sqlalchemy.filter import Filter
from src.models.combination_rule import CombinationRule
from src.models.system import BaseModelo
from src.schemas.filters import FilterModel
from src.schemas.overtime_rule_schemas import (OvertimeRuleIDModel,
                                               OvertimeRuleModel)
from src.schemas.schemas import ScheduleDesviationRuleModel, ZoneModel


class CombinationRuleModel(BaseModelo):
    name: str
    description: str
    default: bool

class CombinationRuleModelResponse(BaseModelo):
    combination_rule_id: Optional[int]
    name: str
    description: str
    default: bool

    overtime_rules:             Optional[List[OvertimeRuleModel]]
    zones:                      Optional[List[ZoneModel]]
    schedule_desviation_rules:  Optional[List[ScheduleDesviationRuleModel]]

class CombinationRuleDBModel(CombinationRuleModel):
    combination_rule_id: int

    overtime_rules: List[OvertimeRuleIDModel]
    zones: List[ZoneModel]
    schedule_desviation_rules: List[ScheduleDesviationRuleModel]


class CombinationRuleModelCombinations(BaseModelo):
    combination_rule_id: int
    name: str
    description: str
    default: bool

    overtime_rules: List[OvertimeRuleModel]
    zones: List[ZoneModel]
    schedule_desviation_rules: List[ScheduleDesviationRuleModel]
    combinations: List[str]


class CombinationRuleModelInput(BaseModelo):
    name: str
    description: Optional[str]
    default: bool

    overtime_rules: Optional[List[OvertimeRuleModel]]
    zones:  Optional[List[ZoneModel]]
    schedule_desviation_rules:  Optional[List[ScheduleDesviationRuleModel]]

class CombinationRuleModelCreate(CombinationRuleModel):
    overtime_rules: Optional[List[int]] = []
    zones:  Optional[List[int]] = []
    schedule_desviation_rules:  Optional[List[int]] = []

class CombinationRuleModelUpdate(CombinationRuleModelCreate):
    combination_rule_id: int

class CombinationRuleDeleteInput(BaseModelo):
    combination_rule_ids: List[int]


class CombinationRuleModelDeleteResponse(BaseModelo):
    count_deleted: int
    deleted: List[CombinationRuleDBModel]


class CombinationRuleModelFilter(FilterModel):

    combination_rule_id__in: Optional[list[str]] = None

    order_by: List[str] = ["name"]
    search: Optional[str] = None

    class Constants(Filter.Constants):
        model = CombinationRule
        search_model_fields = ["name", "enable"]

class CombinationsDBModel(BaseModelo):
    id: int
    combination_rule_id: int
    # id_a: int
    # id_b: int
    type_a: str
    type_b: str
    # default: Optional[str]
    a: Optional[OvertimeRuleIDModel | ZoneModel | ScheduleDesviationRuleModel]
    b: Optional[OvertimeRuleIDModel | ZoneModel | ScheduleDesviationRuleModel]
    predeterminado: Optional[ OvertimeRuleIDModel | ZoneModel | ScheduleDesviationRuleModel ] = Field(serialization_alias='default')

class CombinationsDBUpdateModel(BaseModelo):
    id: int
    combination_rule_id: int
    default: Optional[str]