import os
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends, Request
from pathlib import Path
from uuid import uuid4
from app.core.security import get_current_user

router = APIRouter(prefix="/upload", tags=["Upload"])

ALLOWED_EXTS = {".png", ".jpg", ".jpeg", ".webp"}
MAX_SIZE_MB = 5

UPLOAD_DIR = Path("static/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

BASE_URL = os.getenv("BASE_URL", "")

@router.post("")
async def upload_image(
    request: Request,
    file: UploadFile = File(...),
    current_user=Depends(get_current_user),
):
    if not file.filename:
        raise HTTPException(status_code=400, detail="Arquivo inválido")

    ext = Path(file.filename).suffix.lower()
    if ext not in ALLOWED_EXTS:
        raise HTTPException(status_code=400, detail=f"Extensão não permitida: {ext}")

    content = await file.read()
    size_mb = len(content) / (1024 * 1024)
    if size_mb > MAX_SIZE_MB:
        raise HTTPException(status_code=400, detail=f"Arquivo acima de {MAX_SIZE_MB}MB")

    name = f"{uuid4().hex}{ext}"
    dest = UPLOAD_DIR / name
    dest.write_bytes(content)

    base = BASE_URL.rstrip("/") if BASE_URL else str(request.base_url).rstrip("/")
    return {"url": f"{base}/static/uploads/{name}"}
