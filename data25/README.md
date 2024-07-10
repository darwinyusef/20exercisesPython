# CRUD - USANDO FastAPI POSTGRESQL RENDER y PSYCOPG2

Bievenidos al CRUD usando fastapi y pyscopg2 para instalar solo debes crear una cuenta en render y modificar la linea

![CRUD](./cliente/img/presentation.gif)

```pyton
def conectar_bd():
    # Agregar siempre ?sslmode=require al final
    conexion = psycopg2.connect(
        "postgresql://user:pass@host.render.com/db?sslmode=require"
    )
```

luego debes instalar venv
```
python -m venv venv
```

luego activar venv (Windows)
```
venv/Scripts/activate
```

luego debes instalar todo
```
pip install
```

luego debes ejecutar 
```
fastapi run main.py
```
Aqui tienes el contenido a nivel de pantallazos 

# UPDATE

![update](./cliente/img/put.jpg)

# GET ALL

![update](./cliente/img/getall.jpg)

# GET / SHOW

![update](./cliente/img/getshow.jpg)


autor @darwinyusef