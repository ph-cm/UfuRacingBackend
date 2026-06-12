from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class SponsorContact(Base):
    __tablename__ = "sponsor_contacts"

    id = Column(Integer, primary_key=True, index=True)

    company_name = Column(String(255), nullable=False)
    responsible_name = Column(String(255), nullable=False)

    email = Column(String(255), nullable=False)
    phone = Column(String(50))

    message = Column(Text)

    status = Column(String(50), default="new")

    created_at = Column(DateTime(timezone=True), server_default=func.now())