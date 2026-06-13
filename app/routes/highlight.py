from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel, ConfigDict
from app.db.session import get_db
from app.models.highlight import Highlight
from app.core.security import require_admin

router = APIRouter(prefix="/highlight", tags=["Highlight"])


class HighlightUpdate(BaseModel):
    member_name: str
    member_role: str
    member_photo: str | None = None
    area_name: str
    area_desc: str
    area_photo: str | None = None


class HighlightResponse(BaseModel):
    id: int
    member_name: str
    member_role: str
    member_photo: str | None = None
    area_name: str
    area_desc: str
    area_photo: str | None = None

    model_config = ConfigDict(from_attributes=True)


@router.get("/", response_model=HighlightResponse)
def get_highlight(db: Session = Depends(get_db)):
    row = db.query(Highlight).first()
    if not row:
        return JSONResponse(status_code=404, content={"detail": "Nenhum destaque encontrado"})
    return row


@router.put("/", response_model=HighlightResponse)
def update_highlight(data: HighlightUpdate, db: Session = Depends(get_db), current_user=Depends(require_admin)):
    row = db.query(Highlight).first()
    if row:
        row.member_name  = data.member_name
        row.member_role  = data.member_role
        row.member_photo = data.member_photo
        row.area_name    = data.area_name
        row.area_desc    = data.area_desc
        row.area_photo   = data.area_photo
    else:
        row = Highlight(**data.model_dump())
        db.add(row)
    db.commit()
    db.refresh(row)
    return row
