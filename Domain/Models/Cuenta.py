from dataclasses import dataclass
from Domain.Models.Saldo import Saldo

@dataclass
class Cuenta:
    id: int
    titular: str
    saldo: Saldo
    tipo: str  
