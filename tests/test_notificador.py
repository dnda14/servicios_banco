from fastapi.testclient import TestClient
from unittest.mock import patch
from notificador.main import app

client = TestClient(app)

def test_enviar_correo_exitoso():
    datos = {
        "destinatario": "prueba@correo.com",
        "asunto": "Test",
        "contenido": "Este es un mensaje de prueba"
    }

    # Simulamos que enviar_correo retorna True (éxito)
    with patch("notificador.main.enviar_correo", return_value=True):
        response = client.post("/notificar", json=datos)
        assert response.status_code == 200
        assert response.json() == {"mensaje": "Correo enviado correctamente"}

def test_enviar_correo_fallido():
    datos = {
        "destinatario": "prueba@correo.com",
        "asunto": "Test",
        "contenido": "Este es un mensaje de prueba"
    }

    # Simulamos que enviar_correo retorna False (fallo)
    with patch("notificador.main.enviar_correo", return_value=False):
        response = client.post("/notificar", json=datos)
        assert response.status_code == 200
        assert response.json() == {"mensaje": "Error al enviar el correo"}
