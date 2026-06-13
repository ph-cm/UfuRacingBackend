from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.member import Member
from app.schemas.member import MemberCreate, MemberUpdate, MemberResponse
from app.core.security import require_admin

router = APIRouter(prefix="/members", tags=["Members"])

@router.get("", response_model=list[MemberResponse])
def list_members(db: Session = Depends(get_db)):
    return db.query(Member).order_by(Member.created_at.desc()).all()

@router.post("", response_model=MemberResponse)
def create_member(data: MemberCreate, db: Session = Depends(get_db), current_user=Depends(require_admin)):
    member = Member(
        name=data.name,
        role=data.role,
        team=data.team,
        photo_url=data.photo_url,
        email=data.email,
        linkedin=data.linkedin,
        birth_date=data.birth_date,
        active=data.active,
    )
    db.add(member)
    db.commit()
    db.refresh(member)
    return member

@router.patch("/{member_id}", response_model=MemberResponse)
def update_member(member_id: int, data: MemberUpdate, db: Session = Depends(get_db), current_user=Depends(require_admin)):
    m = db.query(Member).filter(Member.id == member_id).first()
    if not m:
        raise HTTPException(status_code=404, detail="Membro não encontrado")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(m, field, value)
    db.commit()
    db.refresh(m)
    return m

@router.delete("/{member_id}")
def delete_member(member_id: int, db: Session = Depends(get_db), current_user=Depends(require_admin)):
    m = db.query(Member).filter(Member.id == member_id).first()
    if not m:
        raise HTTPException(status_code=404, detail="Membro não encontrado")
    db.delete(m)
    db.commit()
    return {"ok": True}
