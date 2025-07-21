
from fastapi import FastAPI
from fastapi import Body
import httpx
from fastapi import HTTPException
from fastapi.responses import StreamingResponse

app = FastAPI()

BONITA_URL = "http://localhost:8080/bonita"
USERNAME = "walter.bates"
PASSWORD = "bpm"

@app.get("/bonita-processes")
def get_processes():
    with httpx.Client(base_url=BONITA_URL) as client:
        # 1. Hacer login
        login_data = {
            "username": str(USERNAME),
            "password": str(PASSWORD),
            
        }

        headers_login = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = client.post("/loginservice", data=login_data, headers=headers_login)
        print("Status:", response.status_code)
        print("Body:", response.text)
        print("Cookies:", client.cookies)
        if response.status_code not in (200, 204):
            return {"error": "Login failed", "status": response.status_code}

        # 2. Extraer el token de la cookie
        token = client.cookies.get("X-Bonita-API-Token")
        if not token:
            return {"error": "No se encontró el token X-Bonita-API-Token"}

        # 3. Llamar a la API autenticada usando cookies + token
        headers = {
            "X-Bonita-API-Token": token
        }
        api_response = client.get("/API/bpm/process?c=10&p=0", headers=headers)

        return {
            "status": api_response.status_code,
            "data": api_response.json()
        }
@app.post("/complete-task/{task_id}")
def complete_task(task_id: str):
    with httpx.Client(base_url=BONITA_URL) as client:
        # Login igual que antes...
        login_data = {
            "username": USERNAME,
            "password": PASSWORD
        }
        headers_login = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = client.post("/loginservice", data=login_data, headers=headers_login)
        if response.status_code not in (200, 204):
            return {"error": "Login failed", "status": response.status_code}
        token = client.cookies.get("X-Bonita-API-Token")
        if not token:
            return {"error": "No se encontró el token X-Bonita-API-Token"}
        headers = {
            "X-Bonita-API-Token": token,
            "Content-Type": "application/json"
        }
        # Obtener el ID del usuario
        user_resp = client.get(f"/API/identity/user?f=userName={USERNAME}", headers=headers)
        users = user_resp.json()
        if not users:
            return {"error": "Usuario no encontrado"}
        user_id = users[0]['id']
        # Asignar la tarea si no está asignada
        """ task_resp = client.get(f"/API/bpm/task/{task_id}", headers=headers)
        task = task_resp.json()
        if not task.get("assigned_id"):
            assign_payload = {"assigned_id": user_id}
            assign_resp = client.put(f"/API/bpm/task/{task_id}", headers=headers, json=assign_payload)
            if assign_resp.status_code != 200:
                return {"error": "No se pudo asignar la tarea", "status": assign_resp.status_code, "body": assign_resp.text} """
        # Completar la tarea
        exec_response = client.post(
            f"/API/bpm/userTask/{task_id}/execution?assign=true", 
            headers=headers,
            json={}
            )
        return {
            "status": exec_response.status_code,
            "body": exec_response.text
        }
        
        
@app.get("/user-tasks/{username}")
def user_tasks(username: str):
    with httpx.Client(base_url=BONITA_URL) as client:
        # Login igual que antes
        login_data = {
            "username": USERNAME,
            "password": PASSWORD
        }
        headers_login = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = client.post("/loginservice", data=login_data, headers=headers_login)
        if response.status_code not in (200, 204):
            return {"error": "Login failed", "status": response.status_code}
        token = client.cookies.get("X-Bonita-API-Token")
        if not token:
            return {"error": "No se encontró el token X-Bonita-API-Token"}
        headers = {
            "X-Bonita-API-Token": token
        }
        # Obtener ID del usuario
        user_resp = client.get(f"/API/identity/user?f=userName={username}", headers=headers)
        users = user_resp.json()
        if not users:
            return {"error": "Usuario no encontrado"}
        user_id = users[0]['id']
        # Obtener tareas
        tasks_resp = client.get(f"/API/bpm/task?state=ready&user_id={user_id}", headers=headers)
        return tasks_resp.json()
    


@app.post("/complete-task-with-data/{task_id}")
def complete_task_with_data(task_id: str, data: dict = Body(...)):
    with httpx.Client(base_url=BONITA_URL) as client:
        login_data = {
            "username": USERNAME,
            "password": PASSWORD
        }
        headers_login = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = client.post("/loginservice", data=login_data, headers=headers_login)
        if response.status_code not in (200, 204):
            return {"error": "Login failed", "status": response.status_code}
        token = client.cookies.get("X-Bonita-API-Token")
        if not token:
            return {"error": "No se encontró el token X-Bonita-API-Token"}
        headers = {
            "X-Bonita-API-Token": token,
            "Content-Type": "application/json"
        }
        exec_response = client.post(
            f"/API/bpm/userTask/{task_id}/execution?assign=true",
            headers=headers,
            json=data
        )
        return {
            "status": exec_response.status_code,
            "body": exec_response.text
        }


@app.get("/documentos/{case_id}")
def listar_documentos(case_id: int):
    with httpx.Client(base_url=BONITA_URL) as client:
        # Login igual que en los otros endpoints
        login_data = {
            "username": USERNAME,
            "password": PASSWORD
        }
        headers_login = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = client.post("/loginservice", data=login_data, headers=headers_login)
        if response.status_code not in (200, 204):
            raise HTTPException(status_code=401, detail="Login failed")
        token = client.cookies.get("X-Bonita-API-Token")
        if not token:
            raise HTTPException(status_code=401, detail="No se encontró el token X-Bonita-API-Token")
        headers = {
            "X-Bonita-API-Token": token
        }
        # Obtener documentos del caso
        resp = client.get(f"/API/bpm/caseDocument?f=caseId={case_id}", headers=headers)
        if resp.status_code != 200:
            raise HTTPException(status_code=404, detail="No se encontraron documentos")
        documentos = resp.json()
        resultado = [
            {
                "id": doc["id"],
                "name": doc["name"],
                "fileName": doc["fileName"],
                "url": f"{BONITA_URL}/documentDownload?fileName={doc['fileName']}&docId={doc['id']}"
            }
            for doc in documentos
        ]
        return resultado
    
@app.get("/descargar-documento/{doc_id}")
def descargar_documento(doc_id: str):
    with httpx.Client(base_url=BONITA_URL) as client:
        # Login igual que en los otros endpoints
        login_data = {
            "username": USERNAME,
            "password": PASSWORD
        }
        headers_login = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = client.post("/loginservice", data=login_data, headers=headers_login)
        if response.status_code not in (200, 204):
            raise HTTPException(status_code=401, detail="Login failed")
        token = client.cookies.get("X-Bonita-API-Token")
        if not token:
            raise HTTPException(status_code=401, detail="No se encontró el token X-Bonita-API-Token")
        headers = {
            "X-Bonita-API-Token": token
        }
        # Obtener metadatos del documento
        doc_resp = client.get(f"/API/bpm/caseDocument/{doc_id}", headers=headers)
        if doc_resp.status_code != 200:
            raise HTTPException(status_code=404, detail="Documento no encontrado")
        doc = doc_resp.json()
        # Agregar la URL de descarga completa
        doc["url"] = f"documentDownload?fileName={doc['fileName']}&contentStorageId={doc['contentStorageId']}"
        return doc