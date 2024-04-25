from pydantic import BaseModel

class Usuario(BaseModel):
    id: int = None
    nombre: str
    apellido: str
    correo_electronico: str