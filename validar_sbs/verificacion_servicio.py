from sqlalchemy.orm import Session
from entidad import Verificacion
from request_schema import VerificacionRequest
from response_schema import VerificacionResponse

def verificar_usuario(db: Session, datos: VerificacionRequest) -> VerificacionResponse:
    # Simulamos validación con SBS (esto sería una API externa real en producción)
    # Lógica de validación ficticia
    es_valido = datos.dni.startswith("1")  # por ejemplo, válido si inicia con "1"

    # Guardamos en base de datos
    nueva_verificacion = Verificacion(
        dni=datos.dni,
        nombres=datos.nombres,
        apellidos=datos.apellidos,
        fecha_nacimiento=datos.fecha_nacimiento,
        valido=es_valido
    )
    db.add(nueva_verificacion)
    db.commit()
    db.refresh(nueva_verificacion)

    mensaje = "El usuario es válido para crédito" if es_valido else "El usuario no cumple los criterios"
    return VerificacionResponse(valido=es_valido, mensaje=mensaje)

