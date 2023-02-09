from pydantic import BaseModel, Field
from models.Products import products as productTable
from config.connection import engine


class Product(BaseModel):
    id: int | None = Field(default=None, title="ID",
                           description="ID del producto")
    nombre: str = Field(
        title="Nombre", description="Nombre del producto", max_length=255)
    precio: float = Field(title="Precio", description="Precio del producto")
    url: str = Field(
        title="URL", description="URL del producto", max_length=255)


example_product = Product(nombre="Producto 1", precio=100.00,
                          url="https://www.google.com/image.png").dict()


def existe_producto(id: int):
    with engine.connect() as connection:
        result = connection.execute(productTable.select().where(
            productTable.c.id == id)).fetchall()
        if len(result) == 0:
            return False
    return True
