import smtplib
from email.message import EmailMessage
from app.core.config import settings

def send_sponsor_email(data):
    msg = EmailMessage()
    msg["Subject"] = f"Novo contato de patrocinador: {data.company_name}"
    msg["From"] = settings.EMAIL_FROM
    msg["To"] = settings.EMAIL_FROM

    msg.set_content(f"""
Empresa: {data.company_name}
Contato: {data.contact_name}
Email: {data.email}
Telefone: {data.phone}

Mensagem:
{data.message}
""")

    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.starttls()
        server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
        server.send_message(msg)