from fastapi.testclient import TestClient
from firmar.main import app  # Asegúrate de que la ruta es correcta

client = TestClient(app)

def test_firmar_endpoint_exito():
    payload = {
        "dni": "12345678",
        "contenido": "Contenido de prueba"
    }

    response = client.post("/app/firmador/firmar", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert "firma" in data
    assert data["mensaje"] == "Documento firmado correctamente"
    assert isinstance(data["firma"], str)
    assert len(data["firma"]) == 64  # SHA256

def test_firmar_endpoint_falta_contenido():
    payload = {
        "dni": "12345678"
       
    }

    response = client.post("/firmar", json=payload)

    assert response.status_code == 422  # Unprocessable Entity
    data = response.json()
    assert data["detail"][0]["loc"][-1] == "contenido"
    assert data["detail"][0]["msg"].startswith("field required")

def test_firmar_endpoint_tipo_incorrecto_dni():
    payload = {
        "dni": 12345678,  # Debería ser string
        "contenido": "Texto válido"
    }

    response = client.post("/firmar", json=payload)

    assert response.status_code == 422
    data = response.json()
    assert data["detail"][0]["loc"][-1] == "dni"
    assert "str type" in data["detail"][0]["msg"]
