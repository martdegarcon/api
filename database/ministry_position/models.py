from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime

class MinistryPosition(SQLModel, table=True):
    __tablename__ = "ministry_position"
    uuid: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    name: str
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None 