from typing import Union
from fastapi import FastAPI

app = FastAPI()

def sumar(a):
    return a + 10

@app.get("/")
async def read_main():
    return {"mensaje": "Hola Mundo"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
