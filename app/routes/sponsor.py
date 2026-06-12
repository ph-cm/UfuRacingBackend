from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.sponsor import Sponsor
from app.schemas.sponsor import SponsorCreate, SponsorResponse
from pydantic import BaseModel

router = APIRouter(prefix="/sponsors", tags=["Sponsors"])

class SponsorUpdate(BaseModel):
    name: str | None = None
    logo_url: str | None = None
    website: str | None = None
    active: bool | None = None

@router.get("", response_model=list[SponsorResponse])
def list_sponsors(db: Session = Depends(get_db), active_only: bool = True):
    q = db.query(Sponsor)
    if active_only:
        q = q.filter(Sponsor.active == True)  # noqa: E712
    return q.order_by(Sponsor.id.desc()).all()

@router.post("", response_model=SponsorResponse)
def create_sponsor(data: SponsorCreate, db: Session = Depends(get_db)):
    sponsor = Sponsor(**data.model_dump())
    db.add(sponsor)
    db.commit()
    db.refresh(sponsor)
    return sponsor

@router.put("/{sponsor_id}", response_model=SponsorResponse)
def update_sponsor(sponsor_id: int, data: SponsorUpdate, db: Session = Depends(get_db)):
    sponsor = db.query(Sponsor).filter(Sponsor.id == sponsor_id).first()
    if not sponsor:
        raise HTTPException(status_code=404, detail="Patrocinador não encontrado")

    payload = data.model_dump(exclude_unset=True)
    for k, v in payload.items():
        setattr(sponsor, k, v)

    db.commit()
    db.refresh(sponsor)
    return sponsor

@router.delete("/{sponsor_id}")
def delete_sponsor(sponsor_id: int, db: Session = Depends(get_db)):
    sponsor = db.query(Sponsor).filter(Sponsor.id == sponsor_id).first()
    if not sponsor:
        raise HTTPException(status_code=404, detail="Patrocinador não encontrado")

    db.delete(sponsor)
    db.commit()
    return {"ok": True}