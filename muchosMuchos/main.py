from fastapi import FastAPI
from database import Base, engine, SessionLocal

app = FastAPI()



@app.post("/categorias")
def crear_categoria(categoria: CategoriaSchema):
    categoria_nueva = Categoria(nombre=categoria.nombre)
    SessionLocal.add(categoria_nueva)
    SessionLocal.commit()
    return categoria_nueva

@app.get("/categorias/{id}")
def obtener_categoria(id: int):
    categoria = session.query(Categoria).get(id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

@app.post("/productos")
def crear_producto(producto: ProductoSchema):
    producto_nuevo = Producto(
        nombre=producto.nombre,
        descripcion=producto.descripcion,
        precio=producto.precio,
        categoria_id=producto.categoria_id,
    )
    session.add(producto_nuevo)
    session.commit()
    return producto_nuevo

@app.get("/productos/{id}")
def obtener_producto(id: int):
    producto = session.query(Producto).get(id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto