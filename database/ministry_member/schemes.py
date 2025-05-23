from typing import Optional
from uuid import UUID
from datetime import datetime
from sqlmodel import SQLModel

class MinistryMemberBase(SQLModel):
    politician_uuid: UUID
    ministry_uuid: UUID
    position_uuid: UUID
    is_active: Optional[bool] = True
    reveal_day: Optional[int] = None

class MinistryMemberCreate(MinistryMemberBase):
    pass

class MinistryMemberRead(MinistryMemberBase):
    uuid: UUID
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None

class MinistryMemberUpdate(SQLModel):
    politician_uuid: Optional[UUID] = None
    ministry_uuid: Optional[UUID] = None
    position_uuid: Optional[UUID] = None
    is_active: Optional[bool] = None
    reveal_day: Optional[int] = None 