from pydantic import BaseModel, ConfigDict
from datetime import datetime

class NewsBase(BaseModel):
    title: str
    summary: str
    content: str
    image: str | None = None
    author: str | None = None
    category: str | None = None
    published: bool = True

class NewsCreate(NewsBase):
    pass

class NewsUpdate(BaseModel):
    title: str | None = None
    summary: str | None = None
    content: str | None = None
    image: str | None = None
    author: str | None = None
    category: str | None = None
    published: bool | None = None

class NewsResponse(NewsBase):
    id: int
    slug: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)