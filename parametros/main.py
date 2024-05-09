from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from routers import items

app = FastAPI()

'''app.title = "Documentación y Pruebas"
app.version = "0.0.1"
app.summary = "🥥️ Esta aplicación es una app pequeña y corta nos permitirá definir en codigo todo lo que respecta a la docuementación del backend usando FASTAPI y Swagger usamos esto como base"
app.description = "🍐️ Obten descripciones y pruebas de parametros usando FASTAPI"'''


@app.get("/", tags=["Home"])
def read_root():
    return {"Hello": "World"}

app.include_router(items.router)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Documentación y Pruebas",
        version="0.0.1",
        summary="🍐️ Obten descripciones y pruebas de parametros usando FASTAPI",
        description="🥥️ Esta aplicación es una app pequeña y corta nos permitirá definir en codigo todo lo que respecta a la docuementación del backend usando FASTAPI y Swagger usamos esto como base",
        contact={
            "name": "Contact: Aquicreamos",
            "url": "http://aquicreamos.com",
            "email": "wsgestor@gmail.com",
        },
        terms_of_service= "/",
        license_info={
            "name": "License Info Apache 2.0",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        },
        routes=app.routes
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://scontent.feoh1-1.fna.fbcdn.net/v/t39.30808-6/299327973_488450629952156_8325044600034121460_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeH2AWV-EnD-9C5qXdSr3xYd8PhIscsJTzDw-EixywlPMMGjv9JUFdbkjac6ZKGOyh8&_nc_ohc=G-VGxMRzSdsQ7kNvgF0afiY&_nc_ht=scontent.feoh1-1.fna&oh=00_AYCwDLcEb_xyjbVA693QEYz24ufMo67XFnCtI6scOMHrXw&oe=6642E981"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
