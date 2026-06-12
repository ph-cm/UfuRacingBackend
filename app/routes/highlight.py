from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.highlight import Highlight

router = APIRouter(prefix="/highlight", tags=["Highlight"])

@router.get("/")
def get_highlight(db: Session = Depends(get_db)):
    return db.query(Highlight).first()