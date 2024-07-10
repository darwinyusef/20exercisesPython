from typing import Optional
from pydantic import BaseModel, EmailStr, Field

# UserBase: Defines common user fields.
class UserBase(BaseModel):
    email: str = Field(default="correo@prueba.com")
    codeqr: str = Field(default="codigoqrvalido")
    username: str = Field(default="usernamevalido")
    name: str = Field(default="Usuario Nombre")
    lastname: str = Field(default="Usuario Apellido")
    phone: str = Field(default="310111111")
    instagram: str = Field(default="https://www.instagram.com/usuariovalido/")
    puppy: str = Field(default="Nombre de mascota")
    is_active: bool = True


# UserCreate: Used for creating users, including password.
class UserCreate(UserBase):
    password: str

# UserUpdate: Used for updating users, with an optional password field.
class UserUpdate(UserBase):
    password: Optional[str] = None

# UserOut: Used for updating users, with an id field.
class UserOut(UserBase):
    id: int = Field(default=1)

    class Config:
        orm_mode = True
