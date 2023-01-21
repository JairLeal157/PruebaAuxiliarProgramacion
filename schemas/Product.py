from pydantic import BaseModel


class Product(BaseModel):
    id: int|None = None
    nombre: str
    precio: float
    url: str

