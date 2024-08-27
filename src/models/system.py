import enum
from pydantic import BaseModel, ConfigDict

class DaysNameEnum(str, enum.Enum):
    monday     = 'monday'
    tuesday    = 'tuesday'
    wednesday  = 'wednesday'
    thursday   = 'thursday'
    friday     = 'friday'
    saturday   = 'saturday'
    sunday     = 'sunday'

class DaysIntEnum(enum.IntFlag):
    monday     = 1
    tuesday    = 2
    wednesday  = 4
    thursday   = 8
    friday     = 16
    saturday   = 32
    sunday     = 64

class BaseModelo(BaseModel):

    model_config = ConfigDict(from_attributes=True, str_strip_whitespace=True, defer_build=True)