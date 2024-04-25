class Vehiculo:
  """Define las características generales de un vehículo."""

  def __init__(self, marca, modelo):
    """Inicializa las propiedades del vehículo."""
    self.marca = marca
    self.modelo = modelo

  def arrancar(self):
    """Simula el arranque del vehículo."""
    print(f"El {self.marca} {self.modelo} está arrancando...")