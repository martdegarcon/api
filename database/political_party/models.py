from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime

class PoliticalParty(SQLModel, table=True):
    __tablename__ = "political_party"
    uuid: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    name: str
    description: Optional[str] = None
    numbers: Optional[int] = None
    is_active: bool = True
    reveal_day: Optional[int] = None
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None 