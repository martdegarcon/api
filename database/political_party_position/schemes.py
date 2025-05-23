from typing import Optional
from uuid import UUID
from datetime import datetime
from sqlmodel import SQLModel

class PoliticalPartyPositionBase(SQLModel):
    name: str

class PoliticalPartyPositionCreate(PoliticalPartyPositionBase):
    pass

class PoliticalPartyPositionRead(PoliticalPartyPositionBase):
    uuid: UUID
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None

class PoliticalPartyPositionUpdate(SQLModel):
    name: Optional[str] = None 