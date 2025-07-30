from abc import ABC, abstractmethod
from Domain.Models.Cliente import Verificacion

class IVerificadorServicio(ABC):
    @abstractmethod
    def procesar_verificacion(self, entidad: Verificacion) -> dict:
        pass
