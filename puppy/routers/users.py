from typing import Annotated
from fastapi import APIRouter,  Depends, HTTPException, status, Path, Body
from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate, UserOut, UserUpdate

from database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Usuarios"],
    responses={404: {"description": "Not found"}}
)


# Dependency to get a database session
def get_db_session():
    db = next(get_db())
    yield db


@router.get("/", response_model=list[UserOut],
            summary="Listar todos los usuarios",
            response_description="Los usuarios han sido encontrados satisfactoriamente",
            description="Lista todos los usuarios de la tabla con sus datos más importantes")
def get_all_users(db: Session = Depends(get_db_session)):
    print('Aqui algo para entender si entra')
    db_users = db.query(User).all()
    return db_users


@router.get("/{user_id}",
            response_model=UserOut,
            summary="Listar un usuario por ID",
            response_description="El usuario ha sido encontrado satisfactoriamente",
            description="Lista un los usuario de la tabla con sus datos más importantes"
            )
def read_user(
    user_id:  Annotated[int, Path(description="user_id ID del usuario")],
    db: Session = Depends(get_db_session)
):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user


@router.post("/",
             response_model=UserOut,
             status_code=status.HTTP_201_CREATED,
             summary="Crear un usuario",
             response_description="El usuario ha sido creado satisfactoriamente",
             description="Crea un usuarios a través de un ingreso de datos"
             )
def create_user(user: UserCreate, db: Session = Depends(get_db_session)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")

    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.put("/{user_id}",
            response_model=UserOut,
            summary="Actualiza un usuario",
            response_description="El usuario ha sido actualizado satisfactoriamente",
            description="Actualiza un usuarios a través de un ingreso de datos actualizados con el anterior")
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db_session)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    for field in user.dict().keys():
        setattr(db_user, field, getattr(user, field))

    db.commit()
    db.refresh(db_user)
    return db_user


@router.delete("/{user_id}",
               summary="Elimina un usuario",
               response_description="El usuario ha sido eliminado satisfactoriamente",
               description="Elimina un usuarios a través de un ID")
def delete_user(user_id: int, db: Session = Depends(get_db_session)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    db.delete(db_user)
    db.commit()
    return {"message": "User deleted"}
