from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Presentation.Schemas.VerificadorRequest import VerificacionRequest
from Presentation.Schemas.VerificadorResponse import VerificacionResponse
from Application.Services.VerificadorServicio import verificar_usuario
from Infrastructure.Databases.VerificadorDatabase import get_db  

router = APIRouter()

@router.post("/verificar", response_model=VerificacionResponse)
def verificar(datos: VerificacionRequest, db: Session = Depends(get_db)):
    return verificar_usuario(datos, db)
