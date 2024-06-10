from typing import Optional


class Product:
    def __init__(self, id: Optional[int] = None, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price
