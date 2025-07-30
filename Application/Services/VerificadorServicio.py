from sqlalchemy.orm import Session
from Presentation.Schemas.VerificadorRequest import VerificacionRequest
from Domain.Services.IVerificadorServicio import IVerificadorServicio
from Infrastructure.Persistence.ClienteRepositorio import obtener_verificacion

def verificar_usuario(datos: VerificacionRequest, db: Session, servicio: IVerificadorServicio):
    entidad = obtener_verificacion(db, datos)
    return servicio.procesar_verificacion(entidad)
