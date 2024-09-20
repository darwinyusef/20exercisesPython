from fastapi import FastAPI, HTTPException, Header
from fastapi.responses import HTMLResponse
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import psycopg2
import os 
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Task(BaseModel):
    user_id: int
    title: str
    description: str
    status: str
    category: str
    priority: str
    created_at: datetime = None
    updated_at: datetime = None


"""
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    title VARCHAR(255),
    description TEXT,
    status CHAR(1),
    category VARCHAR(100),
    priority VARCHAR(20),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
"""
DATABASE_URL = os.getenv('PG_APIKEY')
# Conectar a la base de datos
def conectar_bd():
    conexion = psycopg2.connect(
        DATABASE_URL #"postgresql://user:password@localhost/mydatabase"
    )
    return conexion

# Cerrar la conexión
def cerrar_bd(conexion):
    conexion.close()


class Task(BaseModel):
    user_id: int
    title: str
    description: str
    status: str
    category: str
    priority: str
    created_at: datetime = None
    updated_at: datetime = None


# ♣-♥-♦ CREATE - POST (Crear una nueva tarea)
@app.post('/tasks/', response_model=Task)
def create_task(task: Task):
    
    conexion = conectar_bd()
    cursor = conexion.cursor()

    query = """
    INSERT INTO tasks (user_id, title, description, status, category, priority, created_at, updated_at)
    VALUES (%s, %s, %s, %s, %s, %s, NOW(), NOW()) RETURNING *;
    """

    cursor.execute(query, (
        task.user_id, task.title, task.description, task.status, task.category, task.priority
    ))

    new_task = cursor.fetchone()
    conexion.commit()
    cursor.close()
    conexion.close()

    return dict(zip([desc[0] for desc in cursor.description], new_task))

# doc, url, sql, front
# ♣-♥-♦ READ - GET (Obtener todas las tareas)
@app.get('/tasks/')
def get_tasks(tocken: Annotated[str | None, Header()] = None):
    
    if tocken == "tocken": 
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tasks;")
        tasks = cursor.fetchall()
        cursor.close()
        conexion.close()
        return [dict(zip([desc[0] for desc in cursor.description], task)) for task in tasks]
    
    raise HTTPException(status_code=401, detail="Do't have a permissions to request")  
    


# READ - GET by ID (Obtener una tarea por ID)
@app.get('/tasks/{task_id}', response_model=Task)
def get_task(task_id: int):
    conexion = conectar_bd()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM tasks WHERE id = %s;", (task_id,))
    task = cursor.fetchone()
    cursor.close()
    conexion.close()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return dict(zip([desc[0] for desc in cursor.description], task))


# UPDATE - PUT (Actualizar una tarea)
@app.put('/tasks/{task_id}', response_model=Task)
def update_task(task_id: int, task: Task):
    conexion = conectar_bd()
    cursor = conexion.cursor()

    query = """
    UPDATE tasks
    SET user_id = %s, title = %s, description = %s, status = %s, category = %s, priority = %s, updated_at = NOW()
    WHERE id = %s RETURNING *;
    """

    cursor.execute(query, (
        task.user_id, task.title, task.description, task.status, task.category, task.priority, task_id
    ))

    updated_task = cursor.fetchone()
    conexion.commit()
    cursor.close()
    conexion.close()

    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return dict(zip([desc[0] for desc in cursor.description], updated_task))


# DELETE - DELETE (Eliminar una tarea)
@app.delete('/tasks/{task_id}', response_model=dict)
def delete_task(task_id: int):
    conexion = conectar_bd()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = %s RETURNING id;", (task_id,))
    deleted_task = cursor.fetchone()
    conexion.commit()
    cursor.close()
    conexion.close()

    if deleted_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted successfully", "id": deleted_task[0]}