from fastapi import APIRouter, Body, status, HTTPException
from schemas.Product import Product, example_product, existeProducto
from models.Products import products as productTable
from config.connection import engine

product = APIRouter(prefix="/products")

@product.get("/", response_model=list[Product], status_code=status.HTTP_200_OK) 
async def get_products():
    with engine.connect() as connection:
        result = connection.execute(productTable.select()).fetchall()
    
    if len(result) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay productos")
    return result
    
@product.get("/{id}", response_model=Product , status_code=status.HTTP_200_OK)
async def get_product(id:int):    
    with engine.connect() as connection:
        result = connection.execute(productTable.select().where(productTable.c.id == id)).fetchall()
    if(len(result) == 0):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe el producto")
    return result[0]

@product.post("/create", response_model= Product,status_code=status.HTTP_201_CREATED)
async def create_product(product:Product = Body(example=example_product)):
    with engine.connect() as connection:
        product.id = None
        dict_product = product.dict()
        f = connection.execute(productTable.insert().values(dict_product))
        dict_product["id"] = f.lastrowid
    return dict_product

@product.put("/update/{id}", status_code=status.HTTP_201_CREATED, response_model=Product)
async def update_product(id:int, product:Product = Body(example=example_product)):
    if not existeProducto(id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe el producto")
    with engine.connect() as connection:
        product.id = id
        dict_product = product.dict()
        connection.execute(productTable.update().values(dict_product).where(productTable.c.id == id))
    return dict_product

@product.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(id:int):
    if not existeProducto(id): 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe el producto")
    with engine.connect() as connection:
        connection.execute(productTable.delete().where(productTable.c.id == id))
    return

