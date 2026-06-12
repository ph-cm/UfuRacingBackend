from sqlalchemy import Column, Integer, String, Boolean
from app.db.base import Base

class Sponsor(Base):
    __tablename__ = "sponsors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)

    # mantenho snake_case no banco (logo_url) pra bater com schema atual
    logo_url = Column(String(500), nullable=True)
    website = Column(String(500), nullable=True)

    active = Column(Boolean, default=True, nullable=False)