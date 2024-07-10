#Importamos librerias necesarias para conexion a bd y uso de las ventanas
import psycopg2
from tkinter import *

#Conexion a la BD
def connction_bd(host,user,passw,db):
    try:#parametros para la conexion a la bd
        connction = psycopg2.connect(
            host= host,
            user = user,
            password = passw,
            database = db,
        )
        print(f"Connected to DB")
        return connction
    
    except psycopg2.Error as ex:#Exepcion si no hat conexion
        print(f"Error connecting to DB {ex}")
        return None
#----------------------------------------------


#Ejecucion de la consulta SQL
def execute_query(connection, consult):
    try:
        query = connection.cursor()
        query.execute(consult)
        row = query.fetchall()#Hacemos la consulta
    
        query.close()
        return row#Devolvemos lo que esta en la tabla
    except psycopg2.Error as ex:
        print(f"error executing the query {ex}")
        return None#Exepcion si la tabla esta vacia
#----------------------------------------------

#Mostramos resultados en la ventana    
def show_rows(row):
    results = []
    for i in row:
        results.append(f" {i}")#Agregamos todos las filas en un array
        
    window = Tk()#Creamos Ventana y definimos propiedades
    window.title("SQL")
    window.geometry("600x150")
    window.resizable(0,0)
    label = Label(window, text="Resultado de la consulta").pack()
    
    page = Text(window, pady=25)
    page.pack()
        
    
    label = Label(page, text="Cliente", bg="cyan", bd=2, relief="solid")
    label.place(x=15,y=-25)

    label = Label(page, text="Total Gastado", bg="cyan", bd=2, relief="solid")
    label.place(x=70,y=-25)
    
    label = Label(page, text="""Esta consulta calculará el total gastado por cada cliente 
sumando el producto de la cantidad y el precio unitario 
                    de cada detalle de pedido en todos sus pedidos.""", bd=2, relief="solid")
    label.place(x=100,y=50)
    
    for i in results:
        page.insert(END, i + "\n")#Mostramos datos en la ventada
            
    window.mainloop()#llamamos la ventana



connect = connction_bd("localhost","postgres","admin","store_test")#llamamos la coneccion a la bd con sus parametros

    
if connect:# si la conn es exitosa, se ejecuta la consulta
    query = (
        """SELECT customers.name, SUM(order_details.amount * order_details.single_price) AS total_spent
            FROM customers
            INNER JOIN orders ON customers.cust_id = orders.cust_id
            INNER JOIN order_details ON orders.order_id = order_details.order_id
            GROUP BY customers.name;"""
        )
    rows = execute_query(connect, query)# almacenamos en rows los resultados de la consulta
    if rows:# si la consulta devuelve algo ejecuta la ventana
        show_rows(rows)#llamamos la venta con los valores que tiene rows

        
        
    connect.close()#Cerramos la conexion a la BD
        
