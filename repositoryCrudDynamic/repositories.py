from typing import List
from models import Usuario
from database import conectar_bd, cerrar_bd

  
class RepositorioUsuario:
    def obtener_todos(self) -> List[Usuario]:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        conexion.commit()
        cerrar_bd(conexion)
        return usuarios

    def crear(self, usuario: Usuario) -> Usuario:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, apellido, correo_electronico) VALUES (%s, %s, %s)", (usuario.nombre, usuario.apellido, usuario.correo_electronico))
        conexion.commit()
        cerrar_bd(conexion)
        return usuario

    def obtener_por_id(self, id: int) -> Usuario:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
        usuario = cursor.fetchone()
        conexion.commit()
        cerrar_bd(conexion)
        return Usuario(**usuario) if usuario else None

    def actualizar(self, usuario: Usuario) -> Usuario:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("UPDATE usuarios SET nombre = %s, apellido = %s, correo_electronico = %s WHERE id = %s", (usuario.nombre, usuario.apellido, usuario.correo_electronico, usuario.id))
        conexion.commit()
        cerrar_bd(conexion)
        return usuario

    def eliminar(self, id: int) -> None:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
        conexion.commit()
        cerrar_bd(conexion)