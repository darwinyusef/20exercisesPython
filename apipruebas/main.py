from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2 

app = FastAPI()
app.title = "CRUD App"

# Para usar Javascript
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=origins,
    allow_headers=origins,
)

class Usuario(BaseModel):
  names: str


def conectar_bd():
    # Agregar siempre ?sslmode=require al final
    conexion = psycopg2.connect(
        "postgres://usersapi_rk0r_user:iBaiCtjVPV63IPeudXOoslwnDjnS5AVB@dpg-col7h0tjm4es738c6cl0-a.oregon-postgres.render.com/usersapi_rk0r?sslmode=require"
    )
    return conexion

def cerrar_bd(conexion):
    conexion.close()


@app.get('/')
def init():
    return {"hola": "mundo"}

# llamamos la url 
@app.get('/alldata', tags=['Names'])
def salida():
    try:
        #Creamos un result vacio
        result = []
        # arrancamos con la conexión a la BD
        conexion = conectar_bd()
        cursor = conexion.cursor()
        # insertamos el sql
        cursor.execute("SELECT * FROM onlydata;")
        usuarios = cursor.fetchall() # Datos
        # printing -> reservado para enviar
        conexion.commit()

        # este codigo es creado por nosotros y nos trae las filas y las columnas y las mezcla
        if cursor.description:
            colnames = [desc[0] for desc in cursor.description] #  Nombres de las columnas
            result = [dict(zip(colnames, row)) for row in usuarios]  
        # cerramos la conexión 
        cerrar_bd(conexion)

        # retornamos el servicio
        return result
    except Exception as e:
        print(f"Error al obtener usuario: {e}")
        return HTMLResponse(status_code=400, content={"mensaje": "Error al obtener los usuarios"})


# llamamos la url 
@app.get('/onlydata/{names}', tags=['Names'])
def salida2(names: str):
    try:
        final = f"SELECT * FROM onlydata WHERE (names) LIKE '%{names}%';"
        # arrancamos con la conexión a la BD
        conexion = conectar_bd()
        cursor = conexion.cursor()
        # insertamos el sql
        cursor.execute(final)
        usuario = cursor.fetchall() # Datos
        # printing -> reservado para enviar
        conexion.commit()
        # este codigo es creado por nosotros y nos trae las filas y las columnas y las mezcla
        respuesta = {
            "mensaje": "Consulta existosa",
            "names": usuario
        }
        return respuesta

        # retornamos el servicio
        return usuarios
    except Exception as e:
        print(f"Error al obtener usuario: {e}")
        return HTMLResponse(status_code=500, content={"mensaje": "Error al obtener los usuarios"})

"""
INSERT INTO onlydata (names) VALUES ('Yusef') RETURNING *
"""

@app.post('/save', tags=['Names'])
def crear(usuario: Usuario):
    try:
        # arrancamos con la conexión a la BD
        conexion = conectar_bd()
        cursor = conexion.cursor()
        # insertamos el sql
        cursor.execute("INSERT INTO onlydata (names) VALUES (%s) RETURNING *",(usuario.names,))
        # printing -> reservado para enviar
        conexion.commit()
        
        usuario_id = cursor.fetchone()[0] # Datos
        
        # cierre de la conexión
        cerrar_bd(conexion)
        
        # se envia ese dato que obtuvimos y se crea la respuesta
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

@app.put('/update/{names}', tags=['Names'])
def crear(usuario: Usuario, names: str):
    try:
        # arrancamos con la conexión a la BD
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("UPDATE onlydata SET names = %s WHERE names = %s RETURNING *;", (usuario.names, names))
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


"""
DELETE FROM onlydata
WHERE (names) = 'Alice';
"""
@app.delete('/delete/{names}', tags=['Names'])
def crear(names: str):
    try:
        final = f"DELETE FROM onlydata WHERE (names) = '{names}';"
        # arrancamos con la conexión a la BD
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute(final)
        conexion.commit()
        cerrar_bd(conexion)
        respuesta = {
            "mensaje": "Usuario eliminado con éxito",
        }
        return respuesta
    
    except Exception as e:
        print(f"Error al crear usuario: {e}")
        return HTMLResponse(status_code=500, content={"mensaje": "Error al crear usuario"})
    
    
def message(): 
    return 'Hola Mundo'