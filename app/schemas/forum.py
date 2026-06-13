from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ForumPostCreate(BaseModel):
    title: str
    content: str

class ForumPostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class ForumAuthor(BaseModel):
    id: int
    name: str
    role: str

    model_config = {"from_attributes": True}

class ForumPostResponse(BaseModel):
    id: int
    title: str
    content: str
    author_id: int
    author: ForumAuthor
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = {"from_attributes": True}
