from datetime import time
from typing import Optional

from pydantic import BaseModel

from ..models.rounding_rule import TypePunchOmitedRoundingEnum


class ConfigPunchInOutInput(BaseModel):
    rounding_rule_id: Optional[int] = None
    in_out: Optional[bool] = None
    early_late: Optional[bool] = None
    change_point: Optional[time] = None
    rounding_extern: Optional[time] = None
    rounding_intern: Optional[time] = None
    grace_period_extern: Optional[time] = None
    grace_period_intern: Optional[time] = None


class ConfigUnplanInput(BaseModel):
    rounding_rule_id: Optional[int] = None
    rounding_entry: Optional[time] = None
    grace_period_entry: Optional[time] = None
    rounding_exit: Optional[time] = None
    grace_period_exit: Optional[time] = None
    rounding_trans: Optional[time] = None
    grace_period_trans: Optional[time] = None

class ConfigPunchOmitted(BaseModel):
    rounding_rule_id: Optional[int] = None
    planified: Optional[bool] = None
    type: Optional[TypePunchOmitedRoundingEnum] = None
    is_exception: Optional[bool] = None

class RoundingRuleInput(BaseModel):
    rounding_rule_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    enable: Optional[bool] = True

class RoundingRuleGeneralInput(BaseModel):
    rounding_rule_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    config_early_punch_in: Optional[ConfigPunchInOutInput] = None
    config_late_punch_in: Optional[ConfigPunchInOutInput] = None
    config_early_punch_out: Optional[ConfigPunchInOutInput] = None
    config_late_punch_out: Optional[ConfigPunchInOutInput] = None
    config_unplan: Optional[ConfigUnplanInput] = None
    config_omited_punch: Optional[ConfigPunchOmitted] = None

