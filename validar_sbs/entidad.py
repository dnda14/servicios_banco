from sqlalchemy import Column, Integer, String, Date, Boolean, DateTime
from database import Base
from datetime import datetime

class Verificacion(Base):
    __tablename__ = "verificaciones"

    id = Column(Integer, primary_key=True, index=True)
    dni = Column(String, index=True)
    nombres = Column(String)
    apellidos = Column(String)
    fecha_nacimiento = Column(Date)
    valido = Column(Boolean)
    fecha_verificacion = Column(DateTime, default=datetime.now)
