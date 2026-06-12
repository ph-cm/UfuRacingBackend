from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
from uuid import uuid4

router = APIRouter(prefix="/upload", tags=["Upload"])

ALLOWED_EXTS = {".png", ".jpg", ".jpeg", ".webp"}
MAX_SIZE_MB = 5

UPLOAD_DIR = Path("static/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("")
async def upload_image(file: UploadFile = File(...)):
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

    # URL pública (você serve /static no main.py)
    return {"url": f"http://127.0.0.1:8000/static/uploads/{name}"}