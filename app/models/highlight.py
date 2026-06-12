# app/models/highlight.py

from sqlalchemy import Column, Integer, String, Text
from app.db.base import Base

class Highlight(Base):
    __tablename__ = "highlights"

    id = Column(Integer, primary_key=True, index=True)

    member_name = Column(String, nullable=False)
    member_role = Column(String, nullable=False)
    member_photo = Column(String, nullable=True)

    area_name = Column(String, nullable=False)
    area_desc = Column(Text, nullable=False)
    area_photo = Column(String, nullable=True)