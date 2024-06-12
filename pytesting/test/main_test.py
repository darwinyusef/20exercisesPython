from server.main import sumar, app
from fastapi.testclient import TestClient

client = TestClient(app)

# Se debe incluir la palabra Test al inicio de la función para hacer el grupping
class TestMain:
    value = 0
    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1
    def test_sumar(self):
        assert sumar(2) == 12
    def test_read_main(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"mensaje": "Hola Mundo"}
    def test_read_item(self):
        response = client.get("/items/2?q=1")
        assert response.status_code == 200
        assert response.json() == {"item_id": 2, "q": "1"}