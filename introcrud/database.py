import psycopg2

'''

        host="dpg-col7h0tjm4es738c6cl0-a.oregon-postgres.render.com",
        database="usersapi_rk0r",
        user="usersapi_rk0r_user",
        password="iBaiCtjVPV63IPeudXOoslwnDjnS5AVB",
        port=5432
    
'''

DATABASE_URL = 'postgres://usersapi_rk0r_user:iBaiCtjVPV63IPeudXOoslwnDjnS5AVB@dpg-col7h0tjm4es738c6cl0-a.oregon-postgres.render.com/usersapi_rk0r'

def conectar_bd():
    conexion = psycopg2.connect(DATABASE_URL)
    return conexion

def cerrar_bd(conexion):
    conexion.close()