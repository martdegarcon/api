from typing import Optional
from uuid import UUID
from datetime import datetime
from sqlmodel import SQLModel

class GovernmentPositionBase(SQLModel):
    name: str

class GovernmentPositionCreate(GovernmentPositionBase):
    pass

class GovernmentPositionRead(GovernmentPositionBase):
    uuid: UUID
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None

class GovernmentPositionUpdate(SQLModel):
    name: Optional[str] = None 