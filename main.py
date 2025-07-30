from fastapi import FastAPI
from Presentation.Controllers.ruta_verificar import verificar
from Infrastructure.Databases.VerificadorDatabase import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(verificar.router, prefix="/verificacion", tags=["Verificación"])
