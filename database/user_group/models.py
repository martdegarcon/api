from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime

class UserGroup(SQLModel, table=True):
    __tablename__ = "user_group"
    uuid: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    name: str
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None 