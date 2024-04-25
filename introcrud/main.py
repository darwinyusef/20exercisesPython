from fastapi import FastAPI
from models import Usuario
from database import conectar_bd, cerrar_bd

app = FastAPI()

@app.get('/')
def message(): 
    return 'Hola Mundo'

def gestionConnect(id: int, usuario: Usuario, sql: str): 
    conexion = conectar_bd()
    cursor = conexion.cursor()
    
    cursor.execute(sql)
    usuarios = cursor.fetchall()
    conexion.commit()
    cerrar_bd(conexion)
    return usuarios


@app.get("/usuarios")
def obtener_usuarios():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conexion.commit()
    cerrar_bd(conexion)
    return usuarios

@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, apellido, correo_electronico) VALUES (%s, %s, %s)", (usuario.nombre, usuario.apellido, usuario.correo_electronico))
    conexion.commit()
    cerrar_bd(conexion)
    return usuario

@app.get("/usuarios/{id}")
def obtener_usuario_por_id(id: int):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
    usuario = cursor.fetchone()
    conexion.commit()
    cerrar_bd(conexion)
    return usuario if usuario else None

@app.put("/usuarios/{id}")
def actualizar_usuario(id: int, usuario: Usuario):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("UPDATE usuarios SET nombre = %s, apellido = %s, correo_electronico = %s WHERE id = %s", (usuario.nombre, usuario.apellido, usuario.correo_electronico, id))
    conexion.commit()
    cerrar_bd(conexion)
    return usuario

@app.delete("/usuarios/{id}")
def eliminar_usuario(id: int):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
    conexion.commit()
    cerrar_bd(conexion)
    return {"mensaje": "Usuario eliminado"}
