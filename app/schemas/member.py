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
    active: bool = True

class MemberCreate(MemberBase):
    pass

class MemberResponse(MemberBase):
    id: int
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)