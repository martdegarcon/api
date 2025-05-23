from typing import Optional
from uuid import UUID
from datetime import datetime
from sqlmodel import SQLModel

class GovernmentBase(SQLModel):
    politician_uuid: UUID
    position_uuid: UUID
    is_active: Optional[bool] = True
    reveal_day: Optional[int] = None

class GovernmentCreate(GovernmentBase):
    pass

class GovernmentRead(GovernmentBase):
    uuid: UUID
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None

class GovernmentUpdate(SQLModel):
    politician_uuid: Optional[UUID] = None
    position_uuid: Optional[UUID] = None
    is_active: Optional[bool] = None
    reveal_day: Optional[int] = None 