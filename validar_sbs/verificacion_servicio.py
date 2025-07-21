from sqlalchemy.orm import Session
from entidad import Verificacion
from request_schema import VerificacionRequest
from response_schema import VerificacionResponse

def verificar_usuario(db: Session, datos: VerificacionRequest) -> VerificacionResponse:
   
    resultado = db.query(Verificacion).filter_by(
        dni=datos.dni,
        nombres=datos.nombres,
        apellidos=datos.apellidos,
        fecha_nacimiento=datos.fecha_nacimiento
    ).first()

    if resultado:
        mensaje = "El usuario es válido para crédito" if resultado.valido else "El usuario no cumple los criterios"
        return VerificacionResponse(valido=resultado.valido, mensaje=mensaje)
    else:
        return VerificacionResponse(valido=False, mensaje="No se encontró información en SBS")

