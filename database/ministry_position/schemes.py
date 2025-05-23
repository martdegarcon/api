from typing import Optional
from uuid import UUID
from datetime import datetime
from sqlmodel import SQLModel

class MinistryPositionBase(SQLModel):
    name: str

class MinistryPositionCreate(MinistryPositionBase):
    pass

class MinistryPositionRead(MinistryPositionBase):
    uuid: UUID
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None

class MinistryPositionUpdate(SQLModel):
    name: Optional[str] = None 