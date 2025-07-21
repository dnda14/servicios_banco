# main.py
from fastapi import FastAPI
from .correo import enviar_correo
from .model import CorreoRequest

app = FastAPI()



@app.post("/notificar")
async def notificar(datos: CorreoRequest):
    enviado = enviar_correo(datos.destinatario, datos.asunto, datos.contenido)
    if enviado:
        return {"mensaje": "Correo enviado correctamente"}
    else:
        return {"mensaje": "Error al enviar el correo"}
