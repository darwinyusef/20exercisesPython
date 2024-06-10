import psycopg2


def conectar_bd():
    # Agregar siempre ?sslmode=require al final
    conexion = psycopg2.connect(
        "postgres://usersapi_rk0r_user:iBaiCtjVPV63IPeudXOoslwnDjnS5AVB@dpg-col7h0tjm4es738c6cl0-a.oregon-postgres.render.com/usersapi_rk0r?sslmode=require"
    )
    return conexion


def cerrar_bd(conexion):
    conexion.close()


def cursor(sql: str):
    # arrancamos con la conexión a la BD
    conexion = conectar_bd()
    cursor = conexion.cursor()
    # insertamos el sql
    cursor.execute(sql)
    conexion.commit()
    # retornamos el servicio a través de una tupla
    return {
        "cursor": cursor,
        "connection": conexion
    }
