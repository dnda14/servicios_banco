# correo.py
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

# Carga las variables desde el archivo .env
load_dotenv()

REMITENTE = os.getenv("EMAIL_REMITENTE")
CONTRASENA = os.getenv("EMAIL_PASSWORD")

def enviar_correo(destinatario: str, asunto: str, contenido: str):
    mensaje = EmailMessage()
    mensaje["From"] = REMITENTE
    mensaje["To"] = destinatario
    mensaje["Subject"] = asunto
    mensaje.set_content(contenido)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(REMITENTE, CONTRASENA)
            smtp.send_message(mensaje)
        return True
    except Exception as e:
        print("Error al enviar el correo:", e)
        return False
