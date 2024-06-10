import json
import logging
import os
import random

logger = logging.getLogger()
logger.setLevel(logging.INFO)

usuarios = [
    {
        "id": 1,
        "nombre": "Juan",
        "apellido": "Pérez",
        "correo_electronico": "juan.perez@ejemplo.com",
        "contrasenia": "mipass123",
        "telefono": "+57 312 3456789",
        "activo": True,
        "role": "info"
    },
    {
        "id": 2,
        "nombre": "María",
        "apellido": "Gómez",
        "correo_electronico": "maria.gomez@ejemplo.com",
        "contrasenia": "micontraseña",
        "telefono": "+57 310 9876543",
        "activo": False,
        "role": "info"
    },
    {
        "id": 3,
        "nombre": "Ana",
        "apellido": "López",
        "correo_electronico": "ana.lopez@ejemplo.com",
        "contrasenia": "micontraseña123",
        "telefono": "+57 311 1234567",
        "activo": True,
        "role": "info"
    },
    {
        "id": 4,
        "nombre": "Pedro",
        "apellido": "García",
        "correo_electronico": "pedro.garcia@ejemplo.com",
        "contrasenia": "mipass456",
        "telefono": "+57 312 7890123",
        "activo": False,
        "role": "info"
    },
    {
        "id": 5,
        "nombre": "Isabel",
        "apellido": "Martínez",
        "correo_electronico": "isabel.martinez@ejemplo.com",
        "contrasenia": "miclave123",
        "telefono": "+57 313 4567890",
        "activo": True,
        "role": "info"
    },
    {
        "id": 6,
        "nombre": "David",
        "apellido": "Ramírez",
        "correo_electronico": "david.ramirez@ejemplo.com",
        "contrasenia": "mipasssecreto",
        "telefono": "+57 314 2345678",
        "activo": True,
        "role": "info"
    },
    {
        "id": 7,
        "nombre": "Sofia",
        "apellido": "Álvarez",
        "correo_electronico": "sofia.alvarez@ejemplo.com",
        "contrasenia": "micontraseña789",
        "telefono": "+57 315 5678901",
        "activo": False,
        "role": "info"
    },
    {
        "id": 8,
        "nombre": "Carlos",
        "apellido": "Rodríguez",
        "correo_electronico": "carlos.rodriguez@ejemplo.com",
        "contrasenia": "mipass12345",
        "telefono": "+57 316 8901234",
        "activo": True,
        "role": "admin"
    },
]

API_KEY = os.environ['API_KEY']


def lambda_handler(event, context):
    # logger.info(event)
    http = event.get("requestContext").get("http")
    method = http.get("method")
    if method in ["POST", "GET"]:
        headers = event.get("headers")
        key = headers.get("x-api-key")
        # query = event.get("queryStringParameters")
        # getBody = event.get("body")

        # Cache excercise
        cleaned_body = json.dumps(random.choice(usuarios)).replace('\\', '')
        body = json.loads(cleaned_body)

        # cleaned_body = getBody.replace('\\', '')
        # body = json.loads(cleaned_body)

        # if str(key) != API_KEY:
        # return {"statusCode": 401, "body": json.dumps("Unauthorized")}

        return {
            # "query": query.get("info"),
            # "bodyParams": body.get("now"),
            # "info": "lista de usuarios primary del sistema exitosa",
            # "user": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6OSwibW9kdWxlIjoiYWRtaW4iLCJub21icmUiOiJZdXNlZiIsImFwZWxsaWRvIjoiR29uemFsZXoiLCJjb3JyZW9fZWxlY3RyXHUwMGYzbmljbyI6IndzZ2VzdG9yQGdtYWlsLmNvbSIsInRlbGVmb25vIjoiKzU3IDMxMSAxMjM0NTY3IiwiYWN0aXZvIjp0cnVlfQ.1zI4_dOLdwzlF4NmCXS5u452hKbcNI1vRzfDainGVHc",
            # "body": usuarios
            "body": body
        }
    else:
        return {"statusCode": 405, "body": json.dumps("Method Not Allowed")}
