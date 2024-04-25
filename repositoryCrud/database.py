import psycopg2
import os

DATABASE_URL =  os.environ["POSTGRESQL_KEY"]

def conectar_bd():
    conexion = psycopg2.connect(DATABASE_URL)
    return conexion

def cerrar_bd(conexion):
    conexion.close()