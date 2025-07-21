from pydantic import BaseModel
from datetime import date

class VerificacionRequest(BaseModel):
    dni: str
    nombres: str
    apellidos: str
    fecha_nacimiento: date
