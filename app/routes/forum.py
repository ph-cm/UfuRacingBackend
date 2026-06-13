from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.forum import ForumPost
from app.schemas.forum import ForumPostCreate, ForumPostUpdate, ForumPostResponse
from app.core.security import require_member

router = APIRouter(prefix="/forum", tags=["Forum"])

@router.get("", response_model=list[ForumPostResponse])
def list_posts(db: Session = Depends(get_db), current_user=Depends(require_member)):
    return db.query(ForumPost).order_by(ForumPost.created_at.desc()).all()

@router.get("/{post_id}", response_model=ForumPostResponse)
def get_post(post_id: int, db: Session = Depends(get_db), current_user=Depends(require_member)):
    post = db.query(ForumPost).filter(ForumPost.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post não encontrado")
    return post

@router.post("", response_model=ForumPostResponse)
def create_post(data: ForumPostCreate, db: Session = Depends(get_db), current_user=Depends(require_member)):
    post = ForumPost(title=data.title, content=data.content, author_id=current_user.id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

@router.put("/{post_id}", response_model=ForumPostResponse)
def update_post(post_id: int, data: ForumPostUpdate, db: Session = Depends(get_db), current_user=Depends(require_member)):
    post = db.query(ForumPost).filter(ForumPost.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post não encontrado")
    if post.author_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Sem permissão para editar este post")

    if data.title is not None:
        post.title = data.title
    if data.content is not None:
        post.content = data.content

    db.commit()
    db.refresh(post)
    return post

@router.delete("/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db), current_user=Depends(require_member)):
    post = db.query(ForumPost).filter(ForumPost.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post não encontrado")
    if post.author_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Sem permissão para deletar este post")

    db.delete(post)
    db.commit()
    return {"ok": True}
