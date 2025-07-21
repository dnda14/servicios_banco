# modelos/request_schema.py
from pydantic import BaseModel

class SolicitudFirma(BaseModel):
    dni: str
    contenido: str  # contenido del documento a firmar
