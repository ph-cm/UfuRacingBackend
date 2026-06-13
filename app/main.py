from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

from app.routes.news import router as news_router
from app.routes.sponsor import router as sponsor_router
from app.routes.highlight import router as highlight_router
from app.routes.auth import router as auth_router
from app.routes.contact import router as contact_router
from app.routes.upload import router as upload_router
from app.routes.admin_dashboard import router as admin_dashboard_router
from app.routes.member import router as members_router
from app.routes.forum import router as forum_router

from app.db.base import Base
from app.db.session import engine
from app.models import image as _image_model  # noqa: F401 — registers Image table
import os

# Garante que o diretório static existe (para compatibilidade com uploads antigos)
Path("static/uploads").mkdir(parents=True, exist_ok=True)

app = FastAPI()

@app.middleware("http")
async def trust_coolify_proxy(request: Request, call_next):
    if request.headers.get("x-forwarded-proto") == "https":
        request.scope["scheme"] = "https"
    response = await call_next(request)
    # Prevent any proxy/CDN from caching API responses
    if not request.url.path.startswith("/static") and not request.url.path.startswith("/images"):
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response

origins_env = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000")
allow_origins = origins_env.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve arquivos estáticos legados (uploads antigos que ainda existam)
from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth_router)
app.include_router(news_router)
app.include_router(sponsor_router)
app.include_router(highlight_router)
app.include_router(contact_router)
app.include_router(upload_router)
app.include_router(admin_dashboard_router)
app.include_router(members_router)
app.include_router(forum_router)

Base.metadata.create_all(bind=engine)

# Safe column migrations — add missing columns without losing data
from sqlalchemy import text, inspect
def _run_migrations():
    inspector = inspect(engine)
    existing = {col["name"] for col in inspector.get_columns("members")}
    with engine.begin() as conn:
        if "birth_date" not in existing:
            conn.execute(text("ALTER TABLE members ADD COLUMN birth_date VARCHAR(10)"))
        if "active" not in existing:
            conn.execute(text("ALTER TABLE members ADD COLUMN active BOOLEAN NOT NULL DEFAULT true"))

try:
    _run_migrations()
except Exception:
    pass
