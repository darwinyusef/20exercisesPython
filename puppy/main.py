from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import users


tags_metadata = [
    {
        "name": "Usuarios",
        "description": "Administra todos los usuarios del sistema",
        "externalDocs": {
            "description": "Link para documentación externa",
            "url": "https://darwinyusef.github.io/mkdocsthemplate/site/tal-4/",
        },
    },
]


app = FastAPI(
    title="UserSQLAlchemy App",
    description="Bienvenidos a nuestra aplicación web, creada con FastAPI y SQLAlchemy. Disfruta de una experiencia rápida y eficiente, diseñada para brindarte un rendimiento y funcionalidad óptimos",
    summary="Sitio web plantilla de fastapi con sqlalchemy",
    version="1.0.0",
    terms_of_service="https://darwinyusef.github.io/mkdocsthemplate/site/",
    contact={
        "name": "Website de Yusef",
        "url": "https://darwinyusef.github.io",
        "email": "wsgestor@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)

