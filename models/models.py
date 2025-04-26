from sqlalchemy import Column, String, Date, Boolean, ForeignKey, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from database import Base

class Politician(Base):
    __tablename__ = "politician"  # The name of the table in the database

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)  # uuid (UUID, PK)
    name = Column(String(255), nullable=False)  # name (Char(255))
    source_name = Column(String(255))  # source_name (Char(255))
    avatar_path = Column(String(255))  # avatar_path (Char(255))
    birthday = Column(Date)  # birthday (Date)
    #gender_uuid = Column(UUID(as_uuid=True), ForeignKey("dataset_gender.uuid"))  # gender_uuid (UUID, FK -> dataset_gender.uuid)
    #province_uuid = Column(UUID(as_uuid=True), ForeignKey("dataset_province.uuid"))  # province_uuid (UUID, FK -> dataset_province.uuid)
    is_married = Column(Boolean, default=False)  # is_married (Boolean)
    children = Column(Integer)  # children (Integer)
    military_service = Column(Boolean, default=False)  # military_service (Boolean)

    created_at = Column(DateTime(timezone=True), server_default=func.now())  # created_at (DateTime)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())  # updated_at (DateTime)
