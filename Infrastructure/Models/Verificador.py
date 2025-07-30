from sqlalchemy import Column, Integer, String, Date, Boolean, DateTime
from Infrastructure.Databases.VerificadorDatabase import Base  # Asegúrate que el Base viene de tu módulo database
from datetime import datetime

class Verificacion(Base):
    __tablename__ = "verificaciones"

    id = Column(Integer, primary_key=True, index=True)
    dni = Column(String, nullable=False, index=True)
    nombres = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    valido = Column(Boolean, nullable=False)
    fecha_verificacion = Column(DateTime, default=datetime.now)
