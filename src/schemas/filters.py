
from datetime import datetime
from typing import Dict, Generic, List, TypedDict, TypeVar

from sqlalchemy.orm import InstrumentedAttribute

from fastapi_filter.contrib.sqlalchemy.filter import Filter


class FilterModel(Filter):
    pass

class Filters(TypedDict):
    between: List[InstrumentedAttribute | datetime | datetime]
    in_: Dict[InstrumentedAttribute, List]
    filter: FilterModel

T = TypeVar("T")
class ModelFilter(FilterModel, Generic[T]):
    class Constants(Filter.Constants):
        model = T
        search_model_fields = ["name", "public_name"]
