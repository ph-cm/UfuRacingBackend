"""
Script de seed para popular o banco com dados reais da equipe UFU Racing.
Execute na raiz do projeto: python seed.py

Idempotente: pode ser rodado em banco que já tem dados.
- Usuários: só cria se não existirem (por email)
- Membros: apaga todos e reinicia com a lista atual
- Highlight: apaga todos e cria o padrão
- News/Sponsors/Contacts: só insere se a tabela estiver vazia
"""

from app.db.session import SessionLocal
from app.core.security import hash_password
from app.models.user import User
from app.models.member import Member
from app.models.news import News
from app.models.sponsor import Sponsor
from app.models.sponsor_contact import SponsorContact
from app.models.highlight import Highlight
from app.models.forum import ForumPost
from app.db.base import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

db = SessionLocal()

# ── users (skip se já existir) ────────────────────────────────────────────────
def get_or_create_user(name, email, password, role, team):
    u = db.query(User).filter(User.email == email).first()
    if not u:
        u = User(
            name=name,
            email=email,
            hashed_password=hash_password(password),
            role=role,
            team=team,
            is_active=True,
        )
        db.add(u)
        db.flush()
    return u

admin = get_or_create_user("Admin UFU Racing", "admin@ufuracing.com", "admin123", "admin", "Gestão")
user1 = get_or_create_user("Pedro Henrique",   "pedro@ufuracing.com", "user123",  "user",  "Administrativo")
user2 = get_or_create_user("Ana Souza",        "ana@ufuracing.com",   "user123",  "user",  "Projetos")
db.commit()

# ── members: limpa e reinicia ─────────────────────────────────────────────────
db.query(Member).delete()
db.commit()

db.add_all([
    # Capitão
    Member(name="Adão",               role="Capitão",                team="Projetos",              active=True),

    # Diretores Administrativos
    Member(name="Clara Aiko",         role="Diretora Administrativa", team="Administrativo",       active=True),
    Member(name="Daniel",             role="Diretor Administrativo",  team="Administrativo",       active=True),

    # Diretores de Projeto
    Member(name="Bárbara",            role="Diretora de Projeto",    team="Projetos",              active=True),
    Member(name="Guilherme",          role="Diretor de Projeto",     team="Projetos",              active=True),

    # Projetista
    Member(name="Alexandre Lanhoso",  role="Projetista",             team="Projetos",              active=True),

    # Administrativo – D.O.
    Member(name="Cecília",            role="D.O.",                   team="Administrativo",        active=True),
    Member(name="Emily",              role="D.O.",                   team="Administrativo",        active=True),
    Member(name="Luis Henrique",      role="D.O.",                   team="Administrativo",        active=True),

    # Administrativo – Financeiro
    Member(name="Itallo",             role="Financeiro",             team="Administrativo",        active=True),
    Member(name="Maria Fernanda",     role="Financeiro",             team="Administrativo",        active=True),
    Member(name="Pedro Henrique",     role="Financeiro",             team="Administrativo",        active=True),

    # Administrativo – Marketing
    Member(name="Maria Lívia",        role="Marketing",              team="Administrativo",        active=True),
    Member(name="Vitória",            role="Marketing",              team="Administrativo",        active=True),

    # Drivetrain
    Member(name="Ana Luiza",          role="Membro",                 team="Drivetrain",            active=True),
    Member(name="Artur",              role="Membro",                 team="Drivetrain",            active=True),
    Member(name="Maria Luiza",        role="Membro",                 team="Drivetrain",            active=True),
    Member(name="Mozart",             role="Membro",                 team="Drivetrain",            active=True),
    Member(name="Pedro Reatto",       role="Membro",                 team="Drivetrain",            active=True),
    Member(name="Ryan",               role="Membro",                 team="Drivetrain",            active=True),
    Member(name="Yan",                role="Membro",                 team="Drivetrain",            active=True),

    # Elétrica e Telemetria
    Member(name="Eduardo",            role="Membro",                 team="Elétrica e Telemetria", active=True),
    Member(name="Fernando",           role="Membro",                 team="Elétrica e Telemetria", active=True),
    Member(name="Gabriel Rosa",       role="Membro Conselheiro",     team="Elétrica e Telemetria", active=True),
    Member(name="Gabriel Santos",     role="Membro",                 team="Elétrica e Telemetria", active=True),
    Member(name="Gustavo Alves",      role="Membro",                 team="Elétrica e Telemetria", active=True),
    Member(name="Pedro Pompeu",       role="Membro",                 team="Elétrica e Telemetria", active=True),

    # Frame and Body
    Member(name="Alexandre Elias",    role="Membro",                 team="Frame and Body",        active=True),
    Member(name="Evellyn",            role="Membro",                 team="Frame and Body",        active=True),
    Member(name="Felipe",             role="Membro",                 team="Frame and Body",        active=True),
    Member(name="Guilherme Melo",     role="Membro",                 team="Frame and Body",        active=True),
    Member(name="Gustavo Pino",       role="Membro",                 team="Frame and Body",        active=True),
    Member(name="Lucas",              role="Membro",                 team="Frame and Body",        active=True),
    Member(name="Nicole",             role="Membro",                 team="Frame and Body",        active=True),

    # Freio e Ergonomia
    Member(name="Ana Laura",          role="Membro",                 team="Freio e Ergonomia",     active=True),
    Member(name="Gabriel Alteff",     role="Membro",                 team="Freio e Ergonomia",     active=True),
    Member(name="Gabriel Sansaloni",  role="Membro",                 team="Freio e Ergonomia",     active=True),
    Member(name="Rubens",             role="Membro",                 team="Freio e Ergonomia",     active=True),
    Member(name="Samuel",             role="Membro",                 team="Freio e Ergonomia",     active=True),
    Member(name="Vitor",              role="Membro",                 team="Freio e Ergonomia",     active=True),

    # Powertrain
    Member(name="Alicia",             role="Membro",                 team="Powertrain",            active=True),
    Member(name="Gabriel William",    role="Membro",                 team="Powertrain",            active=True),
    Member(name="Henrique",           role="Membro",                 team="Powertrain",            active=True),
    Member(name="Ítalo",              role="Membro",                 team="Powertrain",            active=True),
    Member(name="José Pedro",         role="Membro",                 team="Powertrain",            active=True),
    Member(name="Rayssa",             role="Membro",                 team="Powertrain",            active=True),
    Member(name="Thiago",             role="Membro",                 team="Powertrain",            active=True),

    # Suspensão e Direção
    Member(name="João Inácio",        role="Membro",                 team="Suspensão e Direção",   active=True),
    Member(name="Rafael",             role="Membro",                 team="Suspensão e Direção",   active=True),
    Member(name="Sthéfany",           role="Membro",                 team="Suspensão e Direção",   active=True),
])
db.commit()

# ── highlight: apaga e recria ─────────────────────────────────────────────────
db.query(Highlight).delete()
db.commit()

db.add(Highlight(
    member_name="Adão",
    member_role="Capitão",
    member_photo=None,
    area_name="Projetos",
    area_desc="Responsável pela gestão geral do projeto e liderança da equipe UFU Racing.",
    area_photo=None,
))
db.commit()

# ── news (só se estiver vazio) ────────────────────────────────────────────────
if db.query(News).count() == 0:
    db.add_all([
        News(
            title="UFU Racing conquista pódio na etapa de Brasília",
            slug="ufu-racing-podio-brasilia",
            summary="A equipe UFU Racing terminou em segundo lugar na etapa realizada em Brasília.",
            content="<p>Foi uma corrida intensa com chuva na primeira metade do percurso...</p>",
            author="UFU Racing",
            category="Competição",
            published=True,
        ),
        News(
            title="Novo motor testado com sucesso no banco de provas",
            slug="novo-motor-banco-de-provas",
            summary="A equipe de powertrain finalizou os testes do novo motor com resultados acima do esperado.",
            content="<p>Após três semanas de ajustes, o motor atingiu 78 cavalos de potência...</p>",
            author="UFU Racing",
            category="Engenharia",
            published=True,
        ),
    ])
    db.commit()

# ── sponsors (só se estiver vazio) ───────────────────────────────────────────
if db.query(Sponsor).count() == 0:
    db.add(Sponsor(name="UFU Racing", logo_url=None, website=None, active=True))
    db.commit()

db.close()

print("Seed concluído.")
print()
print("Usuários (admin@ufuracing.com / admin123)")
print(f"Membros inseridos: 53")
print(f"Highlight: Adão / Projetos")
