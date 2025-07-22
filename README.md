<img width="1314" height="619" alt="image" src="https://github.com/user-attachments/assets/880c31b7-0c8c-4cde-bd35-09500f2c100b" />

Notificar usuario
<img width="1354" height="781" alt="image" src="https://github.com/user-attachments/assets/bbe46806-08c6-4a55-90f3-0bc3b99e592a" />
Generar firma
<img width="1361" height="757" alt="image" src="https://github.com/user-attachments/assets/b4be0640-aa9a-49da-b57e-2a8f78239ffe" />
Validar usuario
<img width="1410" height="680" alt="image" src="https://github.com/user-attachments/assets/354823ad-a903-484b-b4a6-c9da31eeffc7" />

Casos 
+--------------+--------------------+------------------------------------+------------------------------------+-------------------------------------------+
| Feature      | Scenario           | Given                              | When                               | Then                                      |
+--------------+--------------------+------------------------------------+------------------------------------+-------------------------------------------+
| Firmador     | Firma exitosa      | Documento y DNI válidos            | Solicitud a /api/firmador/firmar   | Respuesta 200 y firma generada            |
+--------------+--------------------+------------------------------------+------------------------------------+-------------------------------------------+
| Firmador     | DNI inválido       | DNI con formato incorrecto         | Solicitud a /api/firmador/firmar   | Error 400 y mensaje claro                 |
+--------------+--------------------+------------------------------------+------------------------------------+-------------------------------------------+
| Notificación | Envío exitoso      | Datos de notificación válidos      | Solicitud a /notificar             | Respuesta 200 y notificación enviada      |
+--------------+--------------------+------------------------------------+------------------------------------+-------------------------------------------+
| Notificación | Email inválido     | Email mal formado                  | Solicitud a /notificar             | Error 400 y mensaje descriptivo           |
+--------------+--------------------+------------------------------------+------------------------------------+-------------------------------------------+
| SBS          | Validación exitosa | Todos los datos correctos          | Solicitud a /sbs/verificar         | Respuesta 200 y validación OK             |
+--------------+--------------------+------------------------------------+------------------------------------+-------------------------------------------+
| SBS          | Datos incompletos  | Faltan campos obligatorios          | Solicitud a /sbs/verificar         | Error 400 indicando campos faltantes      |
+--------------+--------------------+------------------------------------+------------------------------------+-------------------------------------------+
