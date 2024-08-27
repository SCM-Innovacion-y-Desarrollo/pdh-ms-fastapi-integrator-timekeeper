from typing import Optional

from pydantic import BaseModel


class WorkRuleScheduleDesviationInput(BaseModel):
    work_rule_id:                   Optional[int] = None
    schedule_desviation_rule_id:    Optional[int] = None

class WorkRuleZoneInput(BaseModel):
    work_rule_id:   Optional[int] = None
    zone_id:        Optional[int] = None

class WorkRuleOvertimeInput(BaseModel):
    work_rule_id:       Optional[int] = None
    overtime_rule_id:   Optional[int] = None

class WorkRuleBreakInput(BaseModel):
    work_rule_id:   Optional[int] = None
    break_rule_id:  Optional[int] = None

class WorkRuleBonusInput(BaseModel):
    work_rule_id:   Optional[int] = None
    bonus_rule_id:  Optional[int] = None

class WorkRuleInput(BaseModel):
    work_rule_id:               Optional[int] = None
    name:                       Optional[str] = None
    description:                Optional[str] = None
    excepcion_rule_id:          Optional[int] = None
    paycodes_distribution_id:   Optional[int] = None
    rounding_rule_id:           Optional[int] = None


class WorkRuleGeneralInput(BaseModel):
    work_rule_id:               Optional[int] = None
    name:                       Optional[str] = None
    description:                Optional[str] = None
    excepcion_rule_id:          Optional[int] = None
    paycodes_distribution_id:   Optional[int] = None
    rounding_rule_id:           Optional[int] = None
    bonus:                      Optional[list[int]] = None
    break_rules:                Optional[list[int]] = None
    overtime_rules:             Optional[list[int]] = None
    zones:                      Optional[list[int]] = None
    schedule_desviation_rules:  Optional[list[int]] = None
