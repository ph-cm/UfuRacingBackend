from sqlalchemy import Column, Integer, String, LargeBinary
from app.db.base import Base

class Image(Base):
    __tablename__ = "images"

    id           = Column(Integer, primary_key=True, index=True)
    content_type = Column(String(50), nullable=False)
    data         = Column(LargeBinary, nullable=False)
