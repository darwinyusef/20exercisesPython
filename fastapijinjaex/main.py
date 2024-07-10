from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from starlette import status
#----------------------Librerias necesarias

app = FastAPI()# Instanceaminto del objeto Fastapi
app.mount("/static", StaticFiles(directory="static"), name="static")#llamaos los estilos
templates = Jinja2Templates(directory="templates")#creamos el directorio de los templates

#-------------Creacion de la clase Car con sur atributos
class Car:
    id: int
    make: str
    model: str
    year: int 
    mileage: int
    retail_price: int
    
    def __init__(self,id, make,model, year, mileage, retail_price):#Constructor del objeto
        self.id = id# Instanceamiento de atributos
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.retail_price = retail_price
#----------------------------------------

#--------------------Diccionario de Carros
CARS = [
    Car(1, "Honda", "Civic LX", 2019, f"{30000:,}km", f"${17500:,} USD"),#instanceamiento del objeto Car()
    Car(2, "Toyota", "Corolla LE", 2018, f"{40000:,}km", f"${16000:,} USD"),
    Car(3, "Honda", "Accord EX-L", 2020, f"{25000:,}km", f"${22500:,} USD"),
    Car(4, "Toyota", "Camry SE", 2017, f"{50000:,}km", f"${18500:,} USD"),
    Car(5, "Ford", "Mustang GT", 2016, f"{35000:,}km", f"${27500:,} USD"),
    Car(6, "Tesla", "Model 3", 2021, f"{15000:,}km", f"${38000:,} USD"),
    Car(7, "Nissan", "Altima SV", 2019, f"{28000:,}km", f"${19500:,} USD"),
    Car(8, "Hyundai", "Elantra SEL", 2020, f"{22000:,}km", f"${16500:,} USD"),
    Car(9, "Subaru", "Impreza Sport", 2018, f"{30000:,}km", f"${20500:,} USD"),
    Car(10, "Mazda", "CX-5 Touring", 2019, f"{27000:,}km", f"${24500:,} USD"),    
]
#-----------------------------------------------------

#--------------------Clase que solicita el carro, heredamos BaseModel
class CarRequest(BaseModel):
    id: int = Field(gt=0)
    make: str = Field(min_length=3)
    model: str = Field(min_length=3)
    year: int = Field(gt=2010, lt=2025)# gt = Greater than, lt = less than
    mileage: int = Field(ge=0, lt=120000)#ge = Greater than or equal
    retail_price: int = Field(ge=3000, lt=100000)
#---------------------Fin clase

#--------------------- Calse para eliminar carro por id
class DeleteCarRequest(BaseModel):
    id: int = Field(..., title="Id del carro a eliminar")
#--------------------

#---------------------diccionario de configuraciones del modelo de Pydantic.
mode_config ={
    "json_schema_extra":{
        "ecamples": [
            {
                "make": "Toyota",
                "model": "Rav-4",
                "year": 2021,
                "mileage": 29500,
                "retail_price": 24800
            }
        ]
    }
}
#-------------------------

#----------------------Ruta de la pagina de inicio

@app.get("/", response_class=HTMLResponse)
async def show_welcome_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})#llamamos el Home.html
#-----------------------

#------------- Creacion de la ruta STOCK con metodo GET
@app.get("/stock")
async def show_stock():
    return [car.__dict__ for car in CARS]#devolvemos el objeto CARS como dict
#Se convierte cada objeto Car en un Diccionario
#--------------

#-------------- Muestra los carros por id con metodo GET
@app.get("/stock/{car_id}", status_code=status.HTTP_200_OK)
async def show_car_id(car_id: int = Path(gt=0)):
    for car in CARS:
        if car.id == car_id:#si el id ingresado por el user esta en la bd, returna ese id
            return car# retornamos el resultado
    raise HTTPException(status_code=404, detail="El carro solicitado no esta en inventario") #mensaje de error
#--------------

#-------------- Mosttrar carro por marca con GET
@app.get("/cars/{_make}")
async def show_cars_by_make(_make: str):
    filtered_cars = [car.__dict__ for car in CARS if car.make.lower() == _make.lower()]#si el make ingresado por el user esta en la bd, returna todos los datos con ese make
    if not filtered_cars:# si no hay resultados
        return {"message": f"No se encontraron carros de la marca '{_make}'"}# mensaje de erro
    return {"Carros": filtered_cars}# retornamos el resultado
#-----------------

#--------------- formulario de creacion del carro con GET
@app.get("/add-car-form", response_class=HTMLResponse)
async def add_car_page(request: Request):
    return templates.TemplateResponse("add_car.html", {"request": request})#llamamos el formulario add_car.html
#---------------

#---------------- Crear un nuevo carro con POST
@app.post("/create-car", status_code=status.HTTP_201_CREATED)
async def create_car(car_request: CarRequest):
    for i in range(len(CARS)):# iteramos sobre el diccionario CARS
        if CARS[i].id == car_request.id:# validamos el id que ingreso el usuario
            raise HTTPException(detail="El Id ingresado ya existe")# mensaje de error
        else:
            new_car = Car(**car_request.__dict__)#desempaquetamos el dic car_request como argumentos
                
    CARS.append(find_car_id(new_car))#validamos que no este repetido el id y agregamos
    return {"message": "¡El carro se ha agregado correctamente!"}
    
#---------------

#--------------- Asignacion de id al carro agregado
def find_car_id(car: Car):
    car.id = 1 if len(CARS) == 0 else CARS[-1].id + 1#si CARS esta vacio le agrega 1 si no, toma la ultima posision y agrega el siguiente
    return car
#---------------

#--------------- Formulario de Update a car con GET
@app.get("/update-car-form", response_class=HTMLResponse)
async def update_car_page(request: Request):
    return templates.TemplateResponse("update_car.html", {"request": request})#llamamos el formulario de update_car.html
#----------------

#---------------- Actualizar un Carro con PUT
@app.put("/update-car", status_code=status.HTTP_200_OK)
async def modify_car(car_request: CarRequest):
    for i in range(len(CARS)):# iteramos sobe el diccionario CARS
        if CARS[i].id == car_request.id:#validamos el id que el usuario esta ingresando
            CARS[i].make = car_request.make#si el id conincide, actualiza todos los datos
            CARS[i].model = car_request.model
            CARS[i].year = car_request.year
            CARS[i].mileage = car_request.mileage
            CARS[i].retail_price = car_request.retail_price
            return {"message": "¡El carro se ha actualizado correctamente!"}# mensaje de exito
    raise HTTPException(status_code=404, detail="Carro no encontrado")# mensaje de error
#---------------

#--------------- Formulario Borrar un carro con GET
@app.get("/delete-car-form", response_class=HTMLResponse)
async def delete_car_page(request: Request):
    return templates.TemplateResponse("delete_car.html", {"request": request})#llamamos el form  delete_car.html
#--------------

#------------- eliminar un carro por id con DELETE
@app.delete("/delete-car", status_code=status.HTTP_200_OK)
async def delete_car(car_request: DeleteCarRequest):
    for i in range(len(CARS)):#iteramos sobre el diccionario CARS
        if CARS[i].id == car_request.id:#validamos el id que ingreso el usuario
            CARS.pop(i)#si coinside, lo elimina
            return f"El carro con id {i+1} ha sido borrado"#mensaje de exito
    raise HTTPException(status_code=404, detail="Carro no encontrado")#mensaje de error
#--------------

#-------------- Run the server
"""if __name__ == "__main__":
    uvicorn.run(
        app,
        # reload=True,  # Reload the server when code changes
        host="0.0.0.0",  # host="127.0.0.1",
        port="8080",  #  port=8000,   # Listen on port 8000
        log_level="info",  # Log level
    )"""
#-------------- or 
""" 
#en consola
fastapi dev main.py
"""