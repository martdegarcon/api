from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field
from sqlalchemy import text
import uuid as uuid_pkg

class TimestampModel(SQLModel):
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={
            'server_default': text('current_timestamp(0)')
        }
    )

    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={
            'server_default': text('current_timestamp(0)'),
            'onupdate': text('current_timestamp(0)')
        }
    )

class UUIDScheme(SQLModel):
    uuid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
        sa_column_kwargs={"server_default": text("gen_random_uuid()"), "unique": True},
    ) 