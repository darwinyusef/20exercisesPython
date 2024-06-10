import json
from fastapi import Request, APIRouter, Depends
from fastapi.exceptions import HTTPException
from models import Product
from repositories import ProductRepository

router = APIRouter(
    prefix="/product",
    tags=["product"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


product_repository = ProductRepository(conn_string="...")


@router.get("/")
async def get_products(request: Request):
    products = product_repository.get_all_products()
    return products


@router.get("/{product_id}")
async def get_product(request: Request, product_id: int):
    product = product_repository.get_product_by_id(product_id)
    if product is None:
        return HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/")
async def create_product(request: Request, product: Product):
    new_product = product_repository.create_product(product)
    return new_product


@router.put("/{product_id}")
async def update_product(request: Request, product_id: int, product: Product):
    updated_product = product_repository.update_product(product)
    return updated_product


@router.delete("/{product_id}")
async def delete_product(request: Request, product_id: int):
    product_repository.delete_product(product_id)
    return {"message": "Product deleted"}

