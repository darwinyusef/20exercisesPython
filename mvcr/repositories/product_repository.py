from models import Product
from psycopg2 import connect
from psycopg2.extensions import adapt

class ProductRepository:
    def __init__(self, conn_string):
        self.conn = connect(conn_string)

    def get_all_products(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()

        product_objects = []
        for product in products:
            product_objects.append(Product(**product))

        return product_objects

    def get_product_by_id(self, product_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        product = cursor.fetchone()

        if product is None:
            return None

        return Product(**product)

    def create_product(self, product: Product):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO products (name, price) VALUES (%s, %s)",
            (product.name, product.price)
        )
        self.conn.commit()

        return Product(id=cursor.lastrowid, **product.dict())

    def update_product(self, product: Product):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE products SET name = %s, price = %s WHERE id = %s",
            (product.name, product.price, product.id)
        )
        self.conn.commit()

    def delete_product(self, product_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
        self.conn.commit()