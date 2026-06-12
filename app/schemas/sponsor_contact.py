from pydantic import BaseModel, ConfigDict
from datetime import datetime

class SponsorContactCreate(BaseModel):
    company_name: str
    responsible_name: str
    email: str
    phone: str | None = None
    message: str | None = None

class SponsorContactResponse(SponsorContactCreate):
    id: int
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SponsorContactUpdateStatus(BaseModel):
    status: str  # "new" | "in_progress" | "won" | "lost" | "spam"