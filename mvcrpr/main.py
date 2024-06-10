

from fastapi import FastAPI
from router import names_router, users_controller
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=origins,
    allow_headers=origins,
)


# Rutas online
app.include_router(users_controller.router)
app.include_router(names_router.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
