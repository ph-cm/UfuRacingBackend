from fastapi import FastAPI
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

from app.db.base import Base
from app.db.session import engine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# servir arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth_router)
app.include_router(news_router)
app.include_router(sponsor_router)
app.include_router(highlight_router)
app.include_router(contact_router)

app.include_router(upload_router)
app.include_router(admin_dashboard_router)
app.include_router(members_router)

Base.metadata.create_all(bind=engine)