from fastapi import APIRouter
from controller import names_controller
from models import names_models

router = APIRouter(
    prefix="/names",
    tags=["Names"],
    responses={404: {"description": "Not found"}},
)


@router.get('/')
def nameGetAll():
    return names_controller.allController("SELECT * FROM onlydata;")


@router.get('/{name}')
def nameGetOnly(name: str):
    return names_controller.onlyController(f"SELECT * FROM onlydata WHERE (names) LIKE '%{name}%';")


@router.post('/')
def namePost(usuario: names_models.Usuario):
    return names_controller.saveUpdateController(f"INSERT INTO onlydata (names) VALUES ('{usuario.names}') RETURNING *")


@router.put('/{name}')
def namePut(usuario: names_models.Usuario, names: str):
    return names_controller.saveUpdateController(f"UPDATE onlydata SET names = '{usuario.names}' WHERE names = '{names}' RETURNING *;")

@router.delete('/{names}')
def crear(names: str):
    return names_controller.clearController(f"DELETE FROM onlydata WHERE (names) = '{names}';")
