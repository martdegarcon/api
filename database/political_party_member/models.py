from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime

class PoliticalPartyMember(SQLModel, table=True):
    __tablename__ = "political_party_member"
    uuid: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    politician_uuid: UUID = Field(foreign_key="politician.uuid")
    political_party_uuid: UUID = Field(foreign_key="political_party.uuid")
    position_uuid: Optional[UUID] = Field(default=None, foreign_key="political_party_position.uuid")
    is_active: bool = True
    reveal_day: Optional[int] = None
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None 