from fastapi import APIRouter, Body, status, HTTPException
from schemas.User import existeUser
from schemas.Product import existeProducto
from schemas.Compra import Compra, example_compra
from models.Compras import compras as compraTable
from config.connection import engine


compra = APIRouter(prefix="/compras")




@compra.post("/", response_model= Compra,status_code=status.HTTP_201_CREATED)
async def create_compra(compra:Compra = Body(example=example_compra)):
    if (not existeUser(compra.usuario_id) or not existeProducto(compra.producto_id)):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario o producto no encontrado")
    with engine.connect() as connection:
        dict_compra = compra.dict()
        connection.execute(compraTable.insert().values(dict_compra))
    return dict_compra