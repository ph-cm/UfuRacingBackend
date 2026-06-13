from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

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
from app.models import image as _image_model  # noqa: F401 — ensures table is created
import os

app = FastAPI()

@app.middleware("http")
async def trust_coolify_proxy(request: Request, call_next):
    # O Coolify avisa o FastAPI se a requisição original era HTTPS através desse header
    if request.headers.get("x-forwarded-proto") == "https":
        # Força o FastAPI a entender que o protocolo interno também é HTTPS
        request.scope["scheme"] = "https"
    
    response = await call_next(request)
    return response

# Divide a string em uma lista, separando por vírgula
origins_env = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000")
allow_origins = origins_env.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
