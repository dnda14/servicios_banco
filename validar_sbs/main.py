from fastapi import FastAPI
from database import Base, engine
from ruta_verificar import router as verificar_router

app = FastAPI(title="Servicio de Verificación SBS")

# Crear tablas
Base.metadata.create_all(bind=engine)

# Registrar rutas
app.include_router(verificar_router, prefix="/sbs", tags=["Verificación SBS"])
