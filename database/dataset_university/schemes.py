from typing import Optional
from uuid import UUID
from datetime import datetime
from sqlmodel import SQLModel

class DatasetUniversityBase(SQLModel):
    name: str
    is_foreign: Optional[bool] = None

class DatasetUniversityCreate(DatasetUniversityBase):
    pass

class DatasetUniversityRead(DatasetUniversityBase):
    uuid: UUID
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None

class DatasetUniversityUpdate(SQLModel):
    name: Optional[str] = None
    is_foreign: Optional[bool] = None 