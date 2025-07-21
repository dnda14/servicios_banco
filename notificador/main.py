# main.py
from fastapi import FastAPI
from correo import enviar_correo

app = FastAPI()

@app.get("/notificar")
async def notificar(destinatario: str, asunto: str, mensaje: str):
    enviado = enviar_correo(destinatario, asunto, mensaje)
    if enviado:
        return {"mensaje": "Correo enviado exitosamente"}
    else:
        return {"error": "No se pudo enviar el correo"}
