<img width="1314" height="619" alt="image" src="https://github.com/user-attachments/assets/880c31b7-0c8c-4cde-bd35-09500f2c100b" />

Notificar usuario
<img width="1354" height="781" alt="image" src="https://github.com/user-attachments/assets/bbe46806-08c6-4a55-90f3-0bc3b99e592a" />
Generar firma
<img width="1361" height="757" alt="image" src="https://github.com/user-attachments/assets/b4be0640-aa9a-49da-b57e-2a8f78239ffe" />
Validar usuario
<img width="1410" height="680" alt="image" src="https://github.com/user-attachments/assets/354823ad-a903-484b-b4a6-c9da31eeffc7" />

Casos 


Feature: Como usuario del sistema, quiero firmar documentos digitalmente para que se garantice su validez legal

| Scenario       | Given                                 | When                                      | Then                                                |
|----------------|----------------------------------------|-------------------------------------------|-----------------------------------------------------|
| Firma exitosa  | El documento y el DNI son válidos     | Se realiza una solicitud a /api/firmador/firmar | Se obtiene una respuesta 200 y la firma generada     |
| DNI inválido   | El DNI tiene un formato incorrecto    | Se realiza una solicitud a /api/firmador/firmar | Se obtiene un error 400         |

Feature: Como sistema de mensajería, quiero enviar notificaciones para que los usuarios reciban información relevante a tiempo

| Scenario       | Given                                 | When                               | Then                                                     |
|----------------|----------------------------------------|------------------------------------|----------------------------------------------------------|
| Envío exitoso  | Los datos de notificación son válidos | Se realiza una solicitud a /notificar | Se obtiene una respuesta 200 y la notificación es enviada |
| Email inválido | El email está mal formado             | Se realiza una solicitud a /notificar | Se obtiene un error 400        |

Feature: Como sistema validador, quiero verificar los datos del usuario con la SBS para que se garantice la autenticidad de la información

| Scenario           | Given                                   | When                                  | Then                                                          |
|--------------------|------------------------------------------|---------------------------------------|---------------------------------------------------------------|
| Validación exitosa | Todos los datos enviados son correctos  | Se realiza una solicitud a /sbs/verificar | Se obtiene una respuesta 200 con validación satisfactoria       |
| Datos incompletos  | Faltan campos obligatorios en los datos | Se realiza una solicitud a /sbs/verificar | Se obtiene un error 400           |


Swagger

<img width="1884" height="792" alt="image" src="https://github.com/user-attachments/assets/ff55dff7-5e9e-46e8-accb-cd71d3045099" />

