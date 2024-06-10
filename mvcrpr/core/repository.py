def fetchAllWithDescription(cursor):
    # Creamos un result vacio
    result = []
    selectors = cursor.fetchall()  # Datos
    # printing -> reservado para enviar
    # este codigo es creado por nosotros y nos trae las filas y las columnas y las mezcla
    if cursor.description:
        colnames = [desc[0]
                    # Nombres de las columnas
                    for desc in cursor.description]
        result = [dict(zip(colnames, row)) for row in selectors]

    return result
    
