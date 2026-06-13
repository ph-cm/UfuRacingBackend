"""
Script de seed para popular o banco com dados mockados.
Execute na raiz do projeto:  python seed.py
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

# ── users ──────────────────────────────────────────────────────────────────────
admin = User(
    name="Admin UFU Racing",
    email="admin@ufuracing.com",
    hashed_password=hash_password("admin123"),
    role="admin",
    team="Gestão",
    is_active=True,
)
user1 = User(
    name="Pedro Henrique",
    email="pedro@ufuracing.com",
    hashed_password=hash_password("user123"),
    role="user",
    team="Powertrain",
    is_active=True,
)
user2 = User(
    name="Ana Souza",
    email="ana@ufuracing.com",
    hashed_password=hash_password("user123"),
    role="user",
    team="Chassis",
    is_active=True,
)
db.add_all([admin, user1, user2])
db.commit()
db.refresh(admin)
db.refresh(user1)
db.refresh(user2)

# ── members (conteúdo público da equipe) ───────────────────────────────────────
db.add_all([
    # Capitão
    Member(name="Adão",               role="Capitão",               team="Projetos",              active=True),

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

# ── news ───────────────────────────────────────────────────────────────────────
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
        author="Fernanda Costa",
        category="Engenharia",
        published=True,
    ),
    News(
        title="Processo seletivo 2025 está aberto",
        slug="processo-seletivo-2025",
        summary="Estão abertas as inscrições para o processo seletivo de novos membros da UFU Racing.",
        content="<p>Os interessados devem se inscrever pelo formulário até o dia 30...</p>",
        author="UFU Racing",
        category="Geral",
        published=False,
    ),
])
db.commit()

# ── sponsors ───────────────────────────────────────────────────────────────────
db.add_all([
    Sponsor(name="TechParts Brasil", logo_url=None, website="https://techparts.com.br", active=True),
    Sponsor(name="Aço Forte",        logo_url=None, website=None,                       active=True),
    Sponsor(name="Parceiro Antigo",  logo_url=None, website=None,                       active=False),
])
db.commit()

# ── sponsor_contacts ───────────────────────────────────────────────────────────
db.add_all([
    SponsorContact(
        company_name="Indústria Alfa",
        responsible_name="Roberto Alves",
        email="roberto@alfa.com",
        phone="(34) 99999-1111",
        message="Temos interesse em patrocinar a equipe para a temporada 2025.",
        status="new",
    ),
    SponsorContact(
        company_name="Beta Componentes",
        responsible_name="Mariana Oliveira",
        email="mariana@beta.com",
        phone="(34) 98888-2222",
        message="Podemos fornecer peças de suspensão sem custo em troca de divulgação.",
        status="contacted",
    ),
])
db.commit()

# ── highlights ─────────────────────────────────────────────────────────────────
db.add(Highlight(
    member_name="Adão",
    member_role="Capitão",
    member_photo=None,
    area_name="Projetos",
    area_desc="Responsável pela gestão geral do projeto e liderança da equipe UFU Racing.",
    area_photo=None,
))
db.commit()

# ── forum_posts ────────────────────────────────────────────────────────────────
db.add_all([
    ForumPost(
        title="Dúvida sobre setup de suspensão para pista molhada",
        content="Pessoal, estamos com dificuldade de definir a dureza da barra estabilizadora quando chove. Alguém tem referência de dados das últimas corridas?",
        author_id=user1.id,
    ),
    ForumPost(
        title="Reunião de alinhamento — semana que vem",
        content="Vamos marcar uma reunião geral na quinta às 19h na sala do LAME. Confirmem presença aqui.",
        author_id=admin.id,
    ),
    ForumPost(
        title="Relatório de telemetria — etapa Brasília",
        content="Subi os arquivos da telemetria na pasta compartilhada. Quem for analisar, foca nos dados de temperatura de pneu nas primeiras 5 voltas.",
        author_id=user2.id,
    ),
])
db.commit()

db.close()

print("Seed concluído.")
print()
print("Usuários criados:")
print("  admin@ufuracing.com  /  admin123  (role: admin)")
print("  pedro@ufuracing.com  /  user123   (role: user)")
print("  ana@ufuracing.com    /  user123   (role: user)")
