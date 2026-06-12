from pydantic import BaseModel, ConfigDict

class SponsorBase(BaseModel):
    name: str
    logo_url: str | None = None
    website: str | None = None
    active: bool = True

class SponsorCreate(SponsorBase):
    pass

class SponsorResponse(SponsorBase):
    id: int

    model_config = ConfigDict(from_attributes=True)