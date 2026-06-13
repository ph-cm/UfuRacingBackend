import os
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends, Request
from fastapi.responses import Response
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.db.session import get_db
from app.models.image import Image

router = APIRouter(tags=["Upload"])

ALLOWED_TYPES = {
    "image/png":  ".png",
    "image/jpeg": ".jpg",
    "image/webp": ".webp",
    "image/gif":  ".gif",
}
MAX_SIZE_MB = 5
BASE_URL = os.getenv("BASE_URL", "")


@router.post("/upload")
async def upload_image(
    request: Request,
    file: UploadFile = File(...),
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    content_type = file.content_type or ""
    if content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail=f"Tipo não permitido: {content_type}")

    data = await file.read()
    if len(data) / (1024 * 1024) > MAX_SIZE_MB:
        raise HTTPException(status_code=400, detail=f"Arquivo acima de {MAX_SIZE_MB}MB")

    img = Image(content_type=content_type, data=data)
    db.add(img)
    db.commit()
    db.refresh(img)

    base = (BASE_URL.rstrip("/") if BASE_URL else str(request.base_url).rstrip("/"))
    return {"url": f"{base}/images/{img.id}"}


@router.get("/images/{image_id}")
def serve_image(image_id: int, db: Session = Depends(get_db)):
    img = db.query(Image).filter(Image.id == image_id).first()
    if not img:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")
    return Response(content=img.data, media_type=img.content_type)
