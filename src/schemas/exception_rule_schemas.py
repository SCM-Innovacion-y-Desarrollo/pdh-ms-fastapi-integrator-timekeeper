from typing import List, Optional

from pydantic import BaseModel

from fastapi_filter.contrib.sqlalchemy.filter import Filter
from src.models.exception_rule import ExceptionRule
from src.models.system import BaseModelo
from src.schemas.filters import FilterModel
from src.schemas.paycode_schemas import PaycodeModel


class ExceptionRuleModel(BaseModel):
    exception_rule_id: int
    name: str
    description: str
    not_planning: bool
    long_interval: str
    shortened_shift: str
    in_punch_very_early: str
    in_punch_early: str
    in_punch_late: str
    out_punch_early: str
    out_punch_late: str
    out_punch_very_late: str
    in_paycode_id: int
    out_paycode_id: int
    enable: bool

    in_paycode: PaycodeModel
    out_paycode: PaycodeModel

class ExceptionRuleInput(BaseModel):
    """     name: str
        description: str
        not_planning: bool
        long_interval: str = Field(pattern=hour_regex)
        shortened_shift: str = Field(pattern=hour_regex)
        in_punch_very_early: str = Field(pattern=hour_regex)
        in_punch_early: str = Field(pattern=hour_regex)
        in_punch_late: str = Field(pattern=hour_regex)
        out_punch_early: str = Field(pattern=hour_regex)
        out_punch_late: str = Field(pattern=hour_regex)
        out_punch_very_late: str = Field(pattern=hour_regex)
        in_paycode_id: int
        out_paycode_id: int """

    name: Optional[str] = None
    not_planning: Optional[bool] = None
    long_interval: Optional[str] = None
    shortened_shift: Optional[str] = None
    in_punch_very_early: Optional[str] = None
    in_punch_early: Optional[str] = None
    in_punch_late: Optional[str] = None
    out_punch_early: Optional[str] = None
    out_punch_late: Optional[str] = None
    out_punch_very_late: Optional[str] = None
    in_paycode_id: Optional[int] = None
    out_paycode_id: Optional[int] = None
    description: Optional[str] = None
    enable: Optional[bool] = None

    """ @validator(
        'long_interval',
        'shortened_shift',
        'in_punch_very_early',
        'in_punch_early',
        'in_punch_late',
        'out_punch_early',
        'out_punch_late',
        'out_punch_very_late'
    )
    def validar_formato(cls, v):
        "Valida el formato de la hora en HH:MM"
        return validation_hour(v) """

class ExceptionRuleFilterModel(FilterModel):
    name: Optional[str] = None
    description: Optional[str] = None
    exception_rule_id__in: Optional[list[str]] = None
    between: Optional[List[str]] = None  # Lista de tres elementos: nombre de la columna, valor de inicio, valor final
    in_: Optional[List[str]] = None  # Lista de dos elementos: nombre de la columna, lista de valores
    type: Optional[str] = None  # Tipo de excepción
    order_by: Optional[List[str]] = None  # Lista de nombres de columnas por las cuales ordenar
    search: Optional[str] = None

    active: Optional[bool] = None  # Para filtrar registros activos/inactivos

    class Constants(Filter.Constants):
        model = ExceptionRule
        search_model_fields = ["name", "description"]

class ExceptionRuleModelDeleteInput(BaseModelo):
    exception_rule_ids: List[int]

class ExceptionRuleModelDeleteResponse(BaseModelo):
    count_deleted: int
    deleted: List[ExceptionRuleModel]

