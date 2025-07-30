# Infrastructure/Persistence/ClienteRepositorio.py

from sqlalchemy.orm import Session
from Infrastructure.Models.Verificador import Verificacion  
from Presentation.Schemas.VerificadorRequest import VerificacionRequest

def obtener_verificacion(db: Session, datos: VerificacionRequest):
    return db.query(Verificacion).filter_by(
        dni=datos.dni,
        nombres=datos.nombres,
        apellidos=datos.apellidos,
        fecha_nacimiento=datos.fecha_nacimiento
    ).first()
