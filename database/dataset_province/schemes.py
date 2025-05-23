from typing import Optional
from uuid import UUID
from datetime import datetime
from sqlmodel import SQLModel

class DatasetProvinceBase(SQLModel):
    name: str

class DatasetProvinceCreate(DatasetProvinceBase):
    pass

class DatasetProvinceRead(DatasetProvinceBase):
    uuid: UUID
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None

class DatasetProvinceUpdate(SQLModel):
    name: Optional[str] = None 