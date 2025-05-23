from typing import Optional
from uuid import UUID
from datetime import datetime
from sqlmodel import SQLModel

class PoliticalPartyMemberBase(SQLModel):
    politician_uuid: UUID
    political_party_uuid: UUID
    position_uuid: Optional[UUID] = None
    is_active: Optional[bool] = True
    reveal_day: Optional[int] = None

class PoliticalPartyMemberCreate(PoliticalPartyMemberBase):
    pass

class PoliticalPartyMemberRead(PoliticalPartyMemberBase):
    uuid: UUID
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None

class PoliticalPartyMemberUpdate(SQLModel):
    politician_uuid: Optional[UUID] = None
    political_party_uuid: Optional[UUID] = None
    position_uuid: Optional[UUID] = None
    is_active: Optional[bool] = None
    reveal_day: Optional[int] = None 