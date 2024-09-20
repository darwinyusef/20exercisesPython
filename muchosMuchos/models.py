from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

Base = declarative_base()

class Categoria(Base):
    __tablename__ = "categorias"

    id_categoria = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False, unique=True)

    productos = relationship("Producto", backref="categoria")

class Producto(Base):
    __tablename__ = "productos"

    id_producto = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(Text)
    precio = Column(Numeric(10, 2))
    id_categoria = Column(Integer, ForeignKey("categorias.id_categoria"), nullable=False)

    categoria = relationship("Categoria")