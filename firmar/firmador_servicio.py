# servicios/firmador_service.py
import hashlib
from datetime import datetime

def firmar_documento(dni: str, contenido: str) -> str:
    timestamp = datetime.utcnow().isoformat()
    data_a_firmar = f"{contenido}|{dni}|{timestamp}"
    firma = hashlib.sha256(data_a_firmar.encode()).hexdigest()
    return firma
