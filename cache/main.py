from requests_cache import CachedSession
from dataclasses import dataclass


@dataclass
class User:
    id: int
    role: str
    apellido: str
    correo_electronico: str
    telefono: str
    nombre: str
    contrasenia: str
    activo: str


def main():
    # aqui va un servicio de AWS lambda
    url = ""
    session = CachedSession(
        cache_name="cache/api_request",
        expire_after=1,
        allowable_methods=["GET"],
    )
    response = get_response(url, session)
    user = User(**response)
    print(user)


def get_response(url: str, session: CachedSession) -> dict:
    response = session.get(url)
    return response.json()["body"]


if __name__ == "__main__":
    main()
