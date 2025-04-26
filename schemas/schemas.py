from pydantic import BaseModel
from uuid import UUID
from datetime import date, datetime

class PoliticianBase(BaseModel):
    name: str  # name (Char(255))
    source_name: str | None = None  # source_name (Char(255))
    avatar_path: str | None = None  # avatar_path (Char(255))
    birthday: date | None = None  # birthday (Date)
    is_married: bool | None = None  # is_married (Boolean)
    children: int | None = None  # children (Integer)
    military_service: bool | None = None  # military_service (Boolean)

class PoliticianCreate(PoliticianBase):
    pass

class Politician(PoliticianBase):
    uuid: UUID  # uuid (UUID, PK)
    created_at: datetime  # created_at (DateTime)
    updated_at: datetime | None = None  # updated_at (DateTime)

    class Config:
        orm_mode = True
