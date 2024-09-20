from pydantic import BaseModel, Field, validator
from typing import Optional

class CategoriaSchema(BaseModel):
    nombre: str = Field(..., title="Nombre de la categoría")

class ProductoSchema(BaseModel):
    nombre: str = Field(..., title="Nombre del producto")
    descripcion: Optional[str] = Field(title="Descripción del producto")
    precio: float = Field(..., title="Precio del producto")
    categoria_id: int = Field(..., title="ID de la categoría")

    @validator("precio")
    def precio_positivo(self, valor):
        if valor <= 0:
            raise ValueError("El precio debe ser un número positivo")