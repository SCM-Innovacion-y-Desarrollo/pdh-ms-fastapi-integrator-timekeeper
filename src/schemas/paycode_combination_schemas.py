from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from fastapi_filter.contrib.sqlalchemy.filter import Filter
from ..models.paycode_combination import PaycodeCombination
from ..models.system import BaseModelo
from ..schemas.filters import FilterModel
from ..schemas.paycode_schemas import PaycodeModel


class PaycodeCombinationRPaycodeModel(BaseModel):
    paycode_id: Optional[int] = None
    paycode_combination_id: Optional[int] = None
    start_date: datetime
    end_date: datetime

    paycode: Optional[PaycodeModel] = None

class PaycodeCombinationRPaycodeModelInput(BaseModelo):
    paycode_id: Optional[int] = None
    paycode_combination_id: Optional[int] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None


class PaycodeCombinationModel(BaseModelo):
    paycode_combination_id: int
    name: str
    description: str
    start_date: datetime
    end_date: datetime
    enable: bool

    paycodes: List[PaycodeModel]
    combinations: List[PaycodeCombinationRPaycodeModel]


class PaycodeCombinationModelInput(BaseModelo):
    name: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    enable: Optional[bool] = None

    paycodes: Optional[List[PaycodeModel]] = []


class PaycodeCombinationDeleteInput(BaseModelo):
    paycode_combination_ids: List[int]


class PaycodeCombinationModelDeleteResponse(BaseModelo):
    count_deleted: int
    deleted: List[PaycodeCombinationModel]


class PaycodeCombinationModelFilter(FilterModel):

    paycode_combination_id__in: Optional[list[str]] = None

    order_by: List[str] = ["name"]
    search: Optional[str] = None

    class Constants(Filter.Constants):
        model = PaycodeCombination
        search_model_fields = ["name", "enable"]