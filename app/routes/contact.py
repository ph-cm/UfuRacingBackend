from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.sponsor_contact import SponsorContact
from app.schemas.sponsor_contact import (
    SponsorContactCreate,
    SponsorContactResponse,
    SponsorContactUpdateStatus,
)

router = APIRouter(prefix="/contact", tags=["Contact"])

@router.post("/sponsor", response_model=SponsorContactResponse, status_code=201)
def create_sponsor_contact(data: SponsorContactCreate, db: Session = Depends(get_db)):
    contact = SponsorContact(**data.model_dump())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

@router.get("/sponsor", response_model=list[SponsorContactResponse])
def list_sponsor_contacts(status: str | None = None, db: Session = Depends(get_db)):
    q = db.query(SponsorContact).order_by(SponsorContact.created_at.desc())
    if status:
        q = q.filter(SponsorContact.status == status)
    return q.all()

@router.patch("/sponsor/{contact_id}", response_model=SponsorContactResponse)
def update_sponsor_contact_status(contact_id: int, data: SponsorContactUpdateStatus, db: Session = Depends(get_db)):
    contact = db.query(SponsorContact).filter(SponsorContact.id == contact_id).first()
    if not contact:
        raise HTTPException(status_code=404, detail="Contato não encontrado")

    contact.status = data.status
    db.commit()
    db.refresh(contact)
    return contact