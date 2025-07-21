from pydantic import BaseModel


class CorreoRequest(BaseModel):
    destinatario: str
    asunto: str
    contenido: str