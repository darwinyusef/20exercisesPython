import  mysql.connector#importamos la libreria de mysql

def connection(host, user, passw, bd):#definimos funcion para la conneccion a la BD
    try:
        connect =  mysql.connector.connect(
            host = host,#atributos para la conexion 
            user = user,
            password = passw,
            database = bd
        )
        #print("Connected to DB")
        return connect#Retornamos la conexion
    except  mysql.connector.Error as e:#Error en caso de que la conexion falle
        print(f"Couldn't connect to DB: {e}")
        return None
#------------------------------------------------------------------------------    

def execute_query(connction, prompt):#funcion para prepara y ejecutar los querys
    try:
        query = connction.cursor()
        query.execute(prompt)
        row = query.fetchall()
        query.close()
        
        return row#retornamos el resultado de la consulta
    except mysql.connector.Error as e:
        print(f"Error while executing the query. {e}")#exepcion en caso de error 
        return None
#------------------------------------------------------------------------------    
        
def show_rows(row):#funcion para mostrar los resultados en consola
    results =[]#Arreglo donde almacenamos los resultados
    for i in row:
        results.append(i)
        
    for i in results:#imprimimos los resultados
        print(f"{i}", end="\n")
#------------------------------------------------------------------------------    
        

connect = connection("localhost","root","","vet")#llamamos la conexion


querys = [#Querys a ejecutar
    "SELECT * FROM pet ORDER BY 'name' ASC",
    "SELECT user, role FROM users",
    "SELECT date_in AS 'Fecha de ingreso', description AS 'Historia clinica' FROM history",
    "SELECT DISTINCT procedures FROM p_doctor",
    "SELECT * FROM pet WHERE pet_id = 6",
    "SELECT * FROM history WHERE history_id pet_id = 15",
    "SELECT * FROM p_doctor WHERE price LIKE '2%'",
    "SELECT * FROM users ORDER BY 'name' DESC LIMIT 10",
    "SELECT u.name AS 'Propietario', p.name AS 'Mascota' FROM users u JOIN pet p ON u.user_id = p.pet_id;"

]

#------------------------------------------------------------------------------    

if connect:
    for i,query in enumerate(querys):
        print(f"Ejecutando la consulta N°{i+1}, {query}:", end="\n")

        rows = execute_query(connect,query)#preparamos el query
        if rows:
            show_rows(rows)#Si hay reultados, los mostramos en pantalla
            print("\n")
    
    connect.close()#Cerramos la conexion SQL
