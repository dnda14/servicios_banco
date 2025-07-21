from fastapi.testclient import TestClient
from validar_sbs.main import app

client = TestClient(app)

def test_usuario_valido():
    params = {
        "dni": "12345678",
        "nombres": "Juan",
        "apellidos": "Pérez",
        "fecha_nacimiento": "1990-01-01"
    }
    response = client.post("/sbs/verificar", json=params)
    assert response.status_code == 200
    data = response.json()
    assert "valido" in data
    assert "mensaje" in data

def test_usuario_no_valido():
    params = {
        "dni": "87654321",
        "nombres": "Ana",
        "apellidos": "García",
        "fecha_nacimiento": "1985-05-10"
    }
    response = client.post("/sbs/verificar", json=params)
    assert response.status_code == 200
    data = response.json()
    assert data["valido"] is False
    assert "no cumple" in data["mensaje"].lower() or "no se encontró" in data["mensaje"].lower()

def test_usuario_no_encontrado():
    params = {
        "dni": "00000000",
        "nombres": "Desconocido",
        "apellidos": "SinRegistro",
        "fecha_nacimiento": "2000-12-31"
    }
    response = client.post("/sbs/verificar", json=params)
    assert response.status_code == 200
    data = response.json()
    assert data["valido"] is False
    assert "no se encontró" in data["mensaje"].lower()