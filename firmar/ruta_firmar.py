# rutas/firmar.py
from fastapi import APIRouter
from request_schema import SolicitudFirma
from firmador_servicio import firmar_documento

router = APIRouter()

@router.post("/firmar")
def firmar(solicitud: SolicitudFirma):
    firma = firmar_documento(solicitud.dni, solicitud.contenido)
    return {
        "firma": firma,
        "mensaje": "Documento firmado correctamente"
    }
