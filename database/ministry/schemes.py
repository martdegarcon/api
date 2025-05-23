from typing import Optional
from uuid import UUID
from datetime import datetime
from sqlmodel import SQLModel

class MinistryBase(SQLModel):
    name: str
    description: Optional[str] = None
    numbers: Optional[int] = None
    is_active: Optional[bool] = True
    reveal_day: Optional[int] = None

class MinistryCreate(MinistryBase):
    pass

class MinistryRead(MinistryBase):
    uuid: UUID
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None

class MinistryUpdate(SQLModel):
    name: Optional[str] = None
    description: Optional[str] = None
    numbers: Optional[int] = None
    is_active: Optional[bool] = None
    reveal_day: Optional[int] = None 