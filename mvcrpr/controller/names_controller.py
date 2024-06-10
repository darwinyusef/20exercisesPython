from fastapi.responses import JSONResponse

from core import repository
from config import conection


def allController(sql):
    try:
        cursor = conection.cursor(sql)
        result = repository.fetchAllWithDescription(cursor['cursor'])
        conection.cerrar_bd(cursor['connection'])
        return JSONResponse(status_code=200, content={"mensaje": "Nombres obtenidos con exito", "data": result})
    except Exception as e:
        print(f"Error al obtener usuario: {e}")
        return JSONResponse(status_code=401, content={"mensaje": "Problemas al obtener la información"})


def onlyController(sql):
    try:
        cursor = conection.cursor(sql)
        result = cursor['cursor'].fetchall()
        conection.cerrar_bd(cursor['connection'])
        return JSONResponse(status_code=200, content={"mensaje": "Nombre obtenido con exito", "data": result})
    except Exception as e:
        print(f"Error al obtener usuario: {e}")
        return JSONResponse(status_code=401, content={"mensaje": "Problemas al obtener la información"})


def saveUpdateController(sql):
    try:
        cursor = conection.cursor(sql)
        result = cursor['cursor'].fetchone()[0]
        conection.cerrar_bd(cursor['connection'])
        return JSONResponse(status_code=200, content={"mensaje": "Nombre cargado con exito", "data": result})
    except Exception as e:
        print(f"Error al obtener usuario: {e}")
        return JSONResponse(status_code=401, content={"mensaje": "Problemas al obtener la información"})

def clearController(sql):
    try:
        cursor = conection.cursor(sql)
        conection.cerrar_bd(cursor['connection'])
        return JSONResponse(status_code=200, content={"mensaje": "Nombre eliminado con exito"})
    except Exception as e:
        print(f"Error al obtener usuario: {e}")
        return JSONResponse(status_code=401, content={"mensaje": "Problemas al obtener la información"})
