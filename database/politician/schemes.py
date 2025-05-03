from datetime import date
from typing import Optional
from sqlmodel import SQLModel
from core.schemes import TimestampModel, UUIDScheme

class PoliticianCreate(SQLModel):
    name: str
    source_name: Optional[str] = None
    avatar_path: Optional[str] = None
    birthday: Optional[date] = None
    is_married: Optional[bool] = None
    children: Optional[int] = None
    military_service: Optional[bool] = None

class PoliticianBase(SQLModel):
    name: str
    source_name: Optional[str] = None
    avatar_path: Optional[str] = None
    birthday: Optional[date] = None
    is_married: Optional[bool] = None
    children: Optional[int] = None
    military_service: Optional[bool] = None

class Politician(TimestampModel, PoliticianBase, UUIDScheme, table=True):
    __tablename__ = "politician" 