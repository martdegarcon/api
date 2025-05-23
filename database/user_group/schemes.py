from typing import Optional
from uuid import UUID
from datetime import date, datetime
from sqlmodel import SQLModel

class UserGroupBase(SQLModel):
    name: str
    start_date: Optional[date] = None
    end_date: Optional[date] = None

class UserGroupCreate(UserGroupBase):
    pass

class UserGroupRead(UserGroupBase):
    uuid: UUID
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None

class UserGroupUpdate(SQLModel):
    name: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None 