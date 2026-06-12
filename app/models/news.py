from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255), nullable=False)
    slug = Column(String(255), unique=True, index=True, nullable=False)

    summary = Column(Text, nullable=False)
    content = Column(Text, nullable=False)

    image = Column(String(500))
    author = Column(String(150), default="UFU Racing")
    category = Column(String(100), default="Geral")

    published = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())