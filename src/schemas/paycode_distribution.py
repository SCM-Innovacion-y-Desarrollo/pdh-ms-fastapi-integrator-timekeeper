from typing import List, Optional
from pydantic import BaseModel
from ..schemas.combination_rule_schemas import CombinationRuleModelResponse

class PaycodesDistributionRPaycodeModel(BaseModel):
    paycodes_distribution_id:    Optional[int] = None
    paycode_id:                  Optional[int] = None
    row:                         Optional[int] = None
    column:                      Optional[int] = None

class PaycodesDistributionROvertimeRuleModel(BaseModel):
    paycodes_distribution_r_overtime_rule_id:   Optional[int] = None
    paycodes_distribution_id:                   Optional[int] = None
    overtime_rule_id:                           Optional[int] = None
    column:                                     Optional[int] = None

class PaycodesDistributionRZoneScheduleDesviationModel(BaseModel):
    paycodes_distribution_r_zone_schedule_desviation_id:    Optional[int] = None
    paycodes_distribution_id:                               Optional[int] = None
    zone_id:                                                Optional[int] = None
    schedule_desviation_rule_id:                            Optional[int] = None
    row:                                                    Optional[int] = None

class PaycodeDistributionResponse(BaseModel):
    paycodes_distribution_id:               Optional[int] = None
    name:                                   Optional[str] = None
    description:                            Optional[str] = None
    combination_rule:                       Optional[CombinationRuleModelResponse] = None
    distributions_paycodes:                 Optional[List[PaycodesDistributionRPaycodeModel]] = []

class PaycodeDistributionModel(BaseModel):
    paycodes_distribution_id:               Optional[int] = None
    name:                                   Optional[str] = None
    description:                            Optional[str] = None
    combination_rule_id:                    Optional[int] = None

class PaycodeDistributionGeneralModel(BaseModel):
    paycodes_distribution_id:               Optional[int] = None
    name:                                   Optional[str] = None
    description:                            Optional[str] = None
    combination_rule_id:                    Optional[int] = None

    distributions_zone_schedule_desviation: Optional[List[PaycodesDistributionRZoneScheduleDesviationModel]] = []
    distributions_overtime_rule:            Optional[List[PaycodesDistributionROvertimeRuleModel]] = []
    distributions_paycodes:                 Optional[List[PaycodesDistributionRPaycodeModel]] = []