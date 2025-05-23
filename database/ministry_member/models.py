from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime

class MinistryMember(SQLModel, table=True):
    __tablename__ = "ministry_member"
    uuid: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    politician_uuid: UUID = Field(foreign_key="politician.uuid")
    ministry_uuid: UUID = Field(foreign_key="ministry.uuid")
    position_uuid: UUID = Field(foreign_key="ministry_position.uuid")
    is_active: bool = True
    reveal_day: Optional[int] = None
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None 