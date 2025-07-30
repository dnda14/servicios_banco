from Domain.Models.Cuenta import Cuenta
from Domain.Models.Saldo import Saldo

class CuentaFactory:
    @staticmethod
    def crear_cuenta(id: int, titular: str, monto: float, tipo_moneda: str) -> Cuenta:
        saldo = Saldo(monto=monto, tipo_moneda=tipo_moneda)

        if monto < 1000:
            tipo = "BASICA"
        elif monto < 10000:
            tipo = "PREMIUM"
        else:
            tipo = "VIP"

        return Cuenta(id=id, titular=titular, saldo=saldo, tipo=tipo)
