from pydantic import BaseModel


class Usuario(BaseModel):
    names: str
