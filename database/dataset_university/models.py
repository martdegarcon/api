from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime

class DatasetUniversity(SQLModel, table=True):
    __tablename__ = "dataset_university"
    uuid: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    name: str
    is_foreign: Optional[bool] = None
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None 