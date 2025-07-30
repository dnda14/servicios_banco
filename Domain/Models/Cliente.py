from datetime import datetime

class Verificacion:
    def __init__(self, id, dni, nombres, apellidos, fecha_nacimiento, valido, fecha_verificacion=None):
        self.id = id
        self.dni = dni
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.valido = valido
        self.fecha_verificacion = fecha_verificacion or datetime.now()

