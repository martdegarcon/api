from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime

class PoliticianEducation(SQLModel, table=True):
    __tablename__ = "politician_education"
    uuid: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    politician_uuid: UUID = Field(foreign_key="politician.uuid")
    university_uuid: UUID = Field(foreign_key="dataset_university.uuid")
    sequence_number: Optional[int] = None
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None 