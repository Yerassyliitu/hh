from pydantic import BaseModel, EmailStr
from enum import Enum

class RegularAlertRead(BaseModel):
    id: int
    email: EmailStr
    period: str
    class from_attributes:
        orm_mode = True

class Period(str, Enum):
    daily = "daily"
    weekly = "weekly"

class RegularAlertCreate(BaseModel):
    email: EmailStr
    period: Period
    class from_attributes:
        orm_mode = True
