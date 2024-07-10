from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Usuario(BaseModel):
    names: str

def conectar_bd():
    # Agregar siempre ?sslmode=require al final
    conexion = psycopg2.connect(
        "postgresql://usersapi_rk0r_user:iBaiCtjVPV63IPeudXOoslwnDjnS5AVB@dpg-col7h0tjm4es738c6cl0-a.oregon-postgres.render.com/usersapi_rk0r?sslmode=require"
    )
    return conexion


def cerrar_bd(conexion):
    conexion.close()

@app.get('/')
def init():
    return {"hola": "mundo"}

# GET - ALL - READ/ALL - OBTENER TODOS
@app.get('/alldata', tags=['names'])
def salida():
    # Creamos un result vacio
    result = []
    # arrancamos con la conexión a la BD
    conexion = conectar_bd()
    cursor = conexion.cursor()
    # insertamos el sql
    cursor.execute("SELECT * FROM onlydata")
    usuarios = cursor.fetchall()
    # reservado para enviar
    conexion.commit()

    # este codigo es creado por nosotros y nos trae las filas y las columnas y las mezcla
    if cursor.description:
        colnames = [desc[0] for desc in cursor.description]
        result = [dict(zip(colnames, row)) for row in usuarios]
    # cerramos la conexión
    conexion.close()

    # retornamos el servicio
    return result

# GET - SHOW - READ/SHOW - ID{names} - OBTENER SOLO UNO
@app.get('/onlydata/{names}', tags=['names'])
def salida(names: str):
    # Creamos un result vacio
    result = []
    # arrancamos con la conexión a la BD
    conexion = conectar_bd()
    cursor = conexion.cursor()
    sql = f"SELECT * FROM onlydata WHERE names LIKE '%{names}%'"
    # insertamos el sql
    cursor.execute(sql)
    usuario = cursor.fetchone()
    # reservado para enviar
    print(usuario)
    conexion.commit()
    respuesta = {
        "mensaje": "Este es el usuario con éxito",
        "id": usuario
    }
    conexion.close()

    # retornamos el servicio
    return respuesta

# POST - CREATE - CREAR UNO 
@app.post('/save', tags=['names'])
def crear(usuario: Usuario):
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO onlydata (names) VALUES (%s) RETURNING *", (usuario.names,))
        conexion.commit()
        usuario_id = cursor.fetchone()[0]
        cerrar_bd(conexion)
        respuesta = {
            "mensaje": "Usuario creado con éxito",
            "id": usuario_id
        }
        return respuesta

    except Exception as e:
        print(f"Error al crear usuario: {e}")
        return HTMLResponse(status_code=500, content={"mensaje": "Error al crear usuario"})


"""
UPDATE onlydata
SET names = 'DarwinS'
WHERE names = 'Darwin'
RETURNING *;
"""
# # PUT - ID{names} - UPDATE - ACTUALIZAR 
@app.put('/update/{names}', tags=['names'])
def actualizar(usuario: Usuario, names: str):
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE onlydata SET names = %s WHERE names = %s RETURNING *;", (usuario.names, names))
        conexion.commit()
        update = cursor.fetchone()[0]
        cerrar_bd(conexion)
        respuesta = {
            "mensaje": "Usuario actualizado con éxito",
            "id": update
        }
        return respuesta

    except Exception as e:
        print(f"Error al crear usuario: {e}")
        return HTMLResponse(status_code=500, content={"mensaje": "Error al crear usuario"})

# DELETE - ID{names}
@app.delete('/delete/{names}', tags=['names'])
def delete(names: str):
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        sql = f"DELETE FROM onlydata WHERE names LIKE '%{names}%';"
        cursor.execute(sql)
        conexion.commit()
        respuesta = {
            "info": "ok",
            "mensaje": "Usuario se ha eliminado con exito",
        }
        return respuesta

    except Exception as e:
        print(f"Error al eliminar el usuario: {e}")
        return HTMLResponse(status_code=500, content={"mensaje": "Error al eliminar usuario"})
