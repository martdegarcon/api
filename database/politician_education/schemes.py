from typing import Optional
from uuid import UUID
from datetime import datetime
from sqlmodel import SQLModel

class PoliticianEducationBase(SQLModel):
    politician_uuid: UUID
    university_uuid: UUID
    sequence_number: Optional[int] = None

class PoliticianEducationCreate(PoliticianEducationBase):
    pass

class PoliticianEducationRead(PoliticianEducationBase):
    uuid: UUID
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None

class PoliticianEducationUpdate(SQLModel):
    politician_uuid: Optional[UUID] = None
    university_uuid: Optional[UUID] = None
    sequence_number: Optional[int] = None 