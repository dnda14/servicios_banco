from pydantic import BaseModel

class VerificacionResponse(BaseModel):
    valido: bool
    mensaje: str
