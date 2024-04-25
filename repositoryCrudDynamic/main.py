from fastapi import FastAPI
from models import Usuario
from repositories import RepositorioUsuario

app = FastAPI()

repositorio_usuario = RepositorioUsuario()

@app.get("/usuarios")
def obtener_usuarios():
    return repositorio_usuario.obtener_todos()

@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    return repositorio_usuario.crear(usuario)

@app.get("/usuarios/{id}")
def obtener_usuario_por_id(id: int):
    return repositorio_usuario.obtener_por_id(id)

@app.put("/usuarios/{id}")
def actualizar_usuario(id: int, usuario: Usuario):
    usuario.id = id
    return repositorio_usuario.actualizar(usuario)

@app.delete("/usuarios/{id}")
def eliminar_usuario(id: int):
    repositorio_usuario.eliminar(id)
    return {"mensaje": "Usuario eliminado"}