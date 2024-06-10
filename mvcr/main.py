from fastapi import FastAPI
from .views import product_repository
app = FastAPI()

app.include_router(product_repository.router)

if __name__ == "__main__":
    app.run()
