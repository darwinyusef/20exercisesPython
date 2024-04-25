from vehiculo import Vehiculo

class Coche(Vehiculo):
  #Define las características específicas de un coche.

  def __init__(self, marca, modelo, color):
    #Inicializa las propiedades del coche heredando de Vehiculo y añadiendo nuevas.
    super().__init__(marca, modelo)  # Llama al constructor de la clase padre
    self.color = color

  def acelerar(self, velocidad):
    #Acelera el coche a la velocidad indicada.
    print(f"El {self.marca} {self.modelo} {self.color} está acelerando a {velocidad} km/h...")
    
  def cajaCambios(self, velocidad):
    #Acelera el coche a la velocidad indicada.
    aceleracion = '0 '; 
    cambio = 'neutro';
    if velocidad > 0 and velocidad < 20: 
        aceleracion = "0 y 20 "
        cambio = 'uno'
    elif velocidad > 21 and velocidad < 35: 
        aceleracion = "21 y 35 "
        cambio = 'dos'
    elif velocidad > 36 and velocidad < 50: 
        aceleracion = "36 y 50 "
        cambio = 'tres'
    elif velocidad > 51 and velocidad < 100: 
        aceleracion = "50 a 70 u 80 "
        cambio = 'cuatro'
    elif velocidad > 101 and velocidad < 200: 
        aceleracion = "80 a 200 "
        cambio = 'cuatro'
    else: 
        aceleracion = "reversa 0 - 200 "
        cambio = 'reversa'
    
    print(f"El {self.marca} {self.modelo} {self.color} está acelerando a {aceleracion} km/h desde el cambio {cambio}")