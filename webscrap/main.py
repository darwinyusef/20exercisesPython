from typing import Union

from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


url = "https://lexica.art/?q=productos+de+belleza+para+el+cabello+mujer+real+fotografia+real+fondo+rojo"
app = FastAPI()

@app.get("/beauty")
def read_root():
    r = requests.get(url)
    if(r.status_code != 403): 
        soup = BeautifulSoup(r.content, "html.parser")
        soup.prettify()
        list_elements = soup.find_all("a", class_="inset-0")
        return {'data': str(list_elements)}
    else:
        return {'error': 'denegado'}


@app.get("/selenium")
def read_root():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")
    imagenes = soup.find_all("img", class_="pointer-events-none")
    
    for imagen in imagenes:
        imagen_url = imagen["src"]
        response = requests.get(imagen_url)
        with open(f"imagen-{imagen_url.split('/')[-1]}.jpg", "wb") as f:
            f.write(response.content)
    driver.quit()


    

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}