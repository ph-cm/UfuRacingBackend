from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.db.session import get_db
from app.models.news import News
from app.models.sponsor import Sponsor  # ajuste se seu model tiver outro nome
from app.models.sponsor_contact import SponsorContact  # ajuste se seu model tiver outro nome
from app.models.member import Member  # vamos criar abaixo

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):
    news_count = db.query(func.count(News.id)).scalar() or 0
    sponsors_count = db.query(func.count(Sponsor.id)).scalar() or 0
    members_count = db.query(func.count(Member.id)).scalar() or 0

    pending_contacts = (
        db.query(func.count(SponsorContact.id))
        .filter(SponsorContact.status == "new")
        .scalar()
        or 0
    )

    recent_contacts = (
        db.query(SponsorContact)
        .order_by(SponsorContact.created_at.desc())
        .limit(8)
        .all()
    )

    return {
        "stats": {
            "news": news_count,
            "sponsors": sponsors_count,
            "members": members_count,
            "sponsor_contacts_pending": pending_contacts,
        },
        "recent_sponsor_contacts": recent_contacts,
    }