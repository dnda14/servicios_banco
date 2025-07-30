from Domain.Models.Cliente import Verificacion
from Domain.Services.IVerificadorServicio import IVerificadorServicio

class VerificadorServicio(IVerificadorServicio):
    def procesar_verificacion(self, entidad: Verificacion) -> dict:
        if entidad is None:
            return {"valido": False, "mensaje": "No se encontró información en SBS"}

        mensaje = "El usuario es válido para crédito" if entidad.valido else "El usuario no cumple los criterios"
        return {"valido": entidad.valido, "mensaje": mensaje}

