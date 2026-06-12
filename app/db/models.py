# app/db/models.py
# ESTE ARQUIVO EXISTE APENAS PARA IMPORTAR OS MODELS
# e assim registrar tudo no Base.metadata.

from app.models.news import News  # noqa: F401
from app.models.sponsor import Sponsor  # noqa: F401
from app.models.member import Member  # noqa: F401
from app.models.sponsor_contact import SponsorContact# noqa: F401
from app.models.user import User  # noqa: F401
from app.models.highlight import Highlight  # noqa: F401

# Se tiver highlight:
# from app.models.highlight import Highlight  # noqa: F401