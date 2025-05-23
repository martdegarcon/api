from typing import Optional
from uuid import UUID
from datetime import datetime
from sqlmodel import SQLModel

class DatasetGenderBase(SQLModel):
    name: str

class DatasetGenderCreate(DatasetGenderBase):
    pass

class DatasetGenderRead(DatasetGenderBase):
    uuid: UUID
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None

class DatasetGenderUpdate(SQLModel):
    name: Optional[str] = None 