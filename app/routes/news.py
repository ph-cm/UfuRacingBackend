from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from slugify import slugify

from app.db.session import get_db
from app.models.news import News
from app.schemas.news import NewsCreate, NewsUpdate, NewsResponse
from app.core.security import require_admin

router = APIRouter(prefix="/news", tags=["News"])


def _unique_slug(db: Session, base_slug: str) -> str:
    slug = base_slug
    n = 2
    while db.query(News).filter(News.slug == slug).first() is not None:
        slug = f"{base_slug}-{n}"
        n += 1
    return slug


@router.get("", response_model=list[NewsResponse])
def list_news(
    db: Session = Depends(get_db),
    published: bool | None = Query(True),
    skip: int = 0,
    limit: int = Query(50, le=200),
):
    q = db.query(News)
    if published is not None:
        q = q.filter(News.published == published)
    return q.order_by(News.created_at.desc()).offset(skip).limit(limit).all()


@router.get("/{news_id}", response_model=NewsResponse)
def get_news_by_id(news_id: int, db: Session = Depends(get_db)):
    news = db.query(News).filter(News.id == news_id).first()
    if not news:
        raise HTTPException(status_code=404, detail="Notícia não encontrada")
    return news


@router.get("/slug/{slug}", response_model=NewsResponse)
def get_news_by_slug(slug: str, db: Session = Depends(get_db)):
    news = db.query(News).filter(News.slug == slug).first()
    if not news:
        raise HTTPException(status_code=404, detail="Notícia não encontrada")
    return news


@router.post("", response_model=NewsResponse)
def create_news(data: NewsCreate, db: Session = Depends(get_db), current_user=Depends(require_admin)):
    base_slug = slugify(data.title)
    slug = _unique_slug(db, base_slug)

    news = News(
        title=data.title,
        summary=data.summary,
        content=data.content,
        image=data.image,
        author=data.author or "UFU Racing",
        category=data.category or "Geral",
        published=data.published,
        slug=slug,
    )

    db.add(news)
    db.commit()
    db.refresh(news)
    return news


@router.put("/{news_id}", response_model=NewsResponse)
def update_news(news_id: int, data: NewsUpdate, db: Session = Depends(get_db), current_user=Depends(require_admin)):
    news = db.query(News).filter(News.id == news_id).first()
    if not news:
        raise HTTPException(status_code=404, detail="Notícia não encontrada")

    if data.title is not None and data.title.strip() and data.title != news.title:
        base_slug = slugify(data.title)
        news.slug = _unique_slug(db, base_slug)
        news.title = data.title

    for field in ["summary", "content", "image", "author", "category", "published"]:
        value = getattr(data, field)
        if value is not None:
            setattr(news, field, value)

    db.commit()
    db.refresh(news)
    return news


@router.delete("/{news_id}")
def delete_news(news_id: int, db: Session = Depends(get_db), current_user=Depends(require_admin)):
    news = db.query(News).filter(News.id == news_id).first()
    if not news:
        raise HTTPException(status_code=404, detail="Notícia não encontrada")

    db.delete(news)
    db.commit()
    return {"ok": True}
