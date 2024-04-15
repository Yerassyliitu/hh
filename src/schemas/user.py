from pydantic import EmailStr, BaseModel
from typing import Optional



class UserRead(BaseModel):
    id: int
    email: EmailStr
    role_id: int
    organization_id: Optional[int]

    class from_attributes:
        orm_mode = True


class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    confirm_password: str
    role_id: int
    # organization_id: int

    class from_attributes:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str

    class from_attributes:
        orm_mode = True


class LoginInput(BaseModel):
    email: EmailStr
    password: str

    class from_attributes:
        orm_mode = True


class LoginOutput(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str

    class from_attributes:
        orm_mode = True