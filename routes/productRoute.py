from fastapi import APIRouter

product = APIRouter(prefix="/products")


@product.get("/")
async def get_products():
    return [{"name": "juana"}, {"name": "Jane"}]
    