from fastapi import FastAPI
from .ruta_firmar import firmar, router

app = FastAPI()
app.include_router(router, prefix="/api/firmador")
app.title = "Servicio de Firmado de Documentos"