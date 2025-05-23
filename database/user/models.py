from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID, uuid4

class User(SQLModel, table=True):
    __tablename__ = "user"
    uuid: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    fullname: str
    login: str
    password: str
    group_uuid: UUID = Field(foreign_key="user_group.uuid")
    is_active: bool = True
    created_at: Optional[str] = None
    updated_at: Optional[str] = None 