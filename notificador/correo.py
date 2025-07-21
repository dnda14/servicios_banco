# correo.py
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

# Carga las variables desde el archivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

REMITENTE = os.getenv("EMAIL_REMITENTE")
CONTRASENA = os.getenv("EMAIL_PASSWORD")
print("Remitente:", REMITENTE)
print("Contraseña:", CONTRASENA)
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
