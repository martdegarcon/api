from typing import Optional
from uuid import UUID
from sqlmodel import SQLModel

class UserBase(SQLModel):
    fullname: str
    login: str
    group_uuid: UUID
    is_active: Optional[bool] = True

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    uuid: UUID

class UserUpdate(SQLModel):
    fullname: Optional[str] = None
    login: Optional[str] = None
    password: Optional[str] = None
    group_uuid: Optional[UUID] = None
    is_active: Optional[bool] = None 