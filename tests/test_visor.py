import pytest
from httpx import AsyncClient, ASGITransport
from fastapi.testclient import TestClient
from visor_documento.main import app, UPLOAD_DIR
import os

@pytest.mark.asyncio
async def test_subir_y_ver_archivo():
    test_filename = "archivo_prueba.txt"
    contenido = b"Este es un archivo de prueba."

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post(
            "/upload",
            files={"file": (test_filename, contenido, "text/plain")}
        )
    assert response.status_code == 200
    assert f"'{test_filename}'" in response.json()["mensaje"]

    # Ahora probamos que el archivo se puede ver (GET /view/{filename})
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get(f"/view/{test_filename}")
    assert response.status_code == 200
    assert response.content == contenido

    # Limpieza: borrar archivo subido
    os.remove(UPLOAD_DIR / test_filename)


client = TestClient(app)
def test_ver_archivo_inexistente():
    archivo_inexistente = "no_existe.txt"
    response = client.get(f"/view/{archivo_inexistente}")
    
    assert response.status_code == 404
    assert response.json()["detail"] == "Archivo no encontrado"