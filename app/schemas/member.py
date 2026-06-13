# app/schemas/member.py
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class MemberBase(BaseModel):
    name: str
    role: str
    team: str
    photo_url: str | None = None
    email: str | None = None
    linkedin: str | None = None
    birth_date: str | None = None
    active: bool = True

class MemberCreate(MemberBase):
    pass

class MemberUpdate(BaseModel):
    name: str | None = None
    role: str | None = None
    team: str | None = None
    photo_url: str | None = None
    email: str | None = None
    linkedin: str | None = None
    birth_date: str | None = None
    active: bool | None = None

class MemberResponse(MemberBase):
    id: int
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)