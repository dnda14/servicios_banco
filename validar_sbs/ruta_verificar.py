from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from request_schema import VerificacionRequest
from response_schema import VerificacionResponse
from verificacion_servicio import verificar_usuario
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/verificar", response_model=VerificacionResponse)
def verificar(datos: VerificacionRequest, db: Session = Depends(get_db)):
    return verificar_usuario(db, datos)
