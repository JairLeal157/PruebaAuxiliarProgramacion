from fastapi import APIRouter
from schemas.Product import Product
from models.Products import products as productTable
from config.connection import engine

product = APIRouter(prefix="/products")

@product.get("/")
async def get_products():
    with engine.connect() as connection:
        result = connection.execute(productTable.select()).fetchall()
    return result

@product.get("/{id}")
async def get_product(id:int):
    with engine.connect() as connection:
        result = connection.execute(productTable.select().where(productTable.c.id == id)).fetchall()[0]
    return result
    
@product.post("/create", response_model= Product)
async def create_product(product:Product):
    with engine.connect() as connection:
        product.id = None
        dict_product = product.dict()
        connection.execute(productTable.insert().values(dict_product))
    return product

@product.put("/update/")
async def update_product(product:Product):
    with engine.connect() as connection:
        dict_product = product.dict()
        connection.execute(productTable.update().values(dict_product).where(productTable.c.id == product.id))
    return

@product.delete("/delete/{id}")
async def delete_product(id:int):
    with engine.connect() as connection:
        connection.execute(productTable.delete().where(productTable.c.id == id))
    return

