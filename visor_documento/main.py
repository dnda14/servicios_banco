from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import os
from pathlib import Path

app = FastAPI()

UPLOAD_DIR = Path("archivos")
UPLOAD_DIR.mkdir(exist_ok=True)
@app.get("/")
async def root():
    return {"message": "Funciona"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_location = UPLOAD_DIR / file.filename
    with open(file_location, "wb") as f:
        content = await file.read()
        f.write(content)
    return {"mensaje": f"Archivo '{file.filename}' subido correctamente."}

@app.get("/view/{filename}")
async def view_file(filename: str):
    file_path = UPLOAD_DIR / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    return FileResponse(file_path)
