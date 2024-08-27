from pydantic import BaseModel
from datetime import date

class PunchesModel(BaseModel):
    employee_id: int
    start_date: date
    end_date: date