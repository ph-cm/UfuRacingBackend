# app/models/member.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)  # ✅ int
    name = Column(String(255), nullable=False)
    role = Column(String(255), nullable=False)
    team = Column(String(255), nullable=False)

    photo_url = Column(String(500), nullable=True)
    email = Column(String(255), nullable=True)
    linkedin = Column(String(500), nullable=True)

    active = Column(Boolean, nullable=False, server_default="true")  # ✅ agora existe
    created_at = Column(DateTime(timezone=True), server_default=func.now())