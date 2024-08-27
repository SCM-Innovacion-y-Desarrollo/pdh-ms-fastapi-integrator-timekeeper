from typing import List, Optional

from pydantic import BaseModel

from fastapi_filter.contrib.sqlalchemy.filter import Filter
from ..models.paycodes_distibution import PaycodesDistribution
from ..models.system import BaseModelo
from ..schemas.filters import FilterModel
from ..schemas.overtime_rule_schemas import (OvertimeRuleDBModel,
                                               OvertimeRuleModel)
from ..schemas.paycode_schemas import PaycodeModel
from ..schemas.schemas import (CombinationRuleNameModel,
                                 ScheduleDesviationRuleModel, ZoneModel)


class PaycodesDistributionRPaycode(BaseModel):
    paycodes_distribution_id:    int
    paycode_id:                  int

    paycode:                     PaycodeModel

class PaycodesDistributionROvertimeRuleModel(BaseModel):
    paycodes_distribution_id:    Optional[int]
    overtime_rule_id:            Optional[int]

    overtime_rule:               Optional[OvertimeRuleDBModel]

class PaycodesDistributionRZoneScheduleDesviationModel(BaseModel):
    paycodes_distribution_id:    Optional[int]
    zone_id:                     Optional[int]
    schedule_desviation_rule_id: Optional[int]

    zone:                        Optional[ZoneModel]
    schedule_desviation_rule:    Optional[ScheduleDesviationRuleModel]


class PaycodeDistributionModel(BaseModel):
    paycodes_distribution_id: int
    name: str
    description: str
    combination_rule_id: int
    enable: bool

    distributions_overtime_rule: List[PaycodesDistributionROvertimeRuleModel]
    distributions_paycodes: List[PaycodesDistributionRPaycode]
    distribution_r_zone_schedule_desviation: List[PaycodesDistributionRZoneScheduleDesviationModel]
    combination_rule: CombinationRuleNameModel

class PaycodesDistributionInput(BaseModel):

    name: str
    description: str
    combination_rule_id: int

    distributions_overtime_rule: Optional[List[PaycodesDistributionROvertimeRuleModel]]
    distributions_paycodes: Optional[List[PaycodesDistributionRPaycode]]
    distribution_r_zone_schedule_desviation: Optional[List[PaycodesDistributionRZoneScheduleDesviationModel]]
    combination_rule: CombinationRuleNameModel

class PaycodesDistributionFilterModel(FilterModel):
    name: Optional[str] = None
    description: Optional[str] = None
    paycodes_distribution_id__in: Optional[list[str]] = None
    between: Optional[List[str]] = None  # Lista de tres elementos: nombre de la columna, valor de inicio, valor final
    in_: Optional[List[str]] = None  # Lista de dos elementos: nombre de la columna, lista de valores

    order_by: Optional[List[str]] = None  # Lista de nombres de columnas por las cuales ordenar
    search: Optional[str] = None

    active: Optional[bool] = None  # Para filtrar registros activos/inactivos

    class Constants(Filter.Constants):
        model = PaycodesDistribution
        search_model_fields = ["name", "enable"]


class CombinationRuleModel(BaseModelo):
    combination_rule_id: int
    name: str
    description: str
    default: bool
    overtime_rules: Optional[List[OvertimeRuleModel]] = None
    zones: Optional[List[ZoneModel]] = None
    schedule_desviation_rules: Optional[List[ScheduleDesviationRuleModel]] = None
