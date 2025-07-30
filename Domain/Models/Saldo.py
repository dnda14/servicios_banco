from dataclasses import dataclass

@dataclass(frozen=True)
class Saldo:
    monto: float
    tipo_moneda: str  
