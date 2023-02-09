from pydantic import BaseModel, Field


class Compra(BaseModel):
    usuario_id: int = Field(
        title="ID Usuario", description="ID del usario que compra")
    producto_id: int = Field(
        title="ID Producto", description="ID del producto comprado")
    total_productos: int = Field(
        title="Cantidad", description="Cantidad de productos comprados")


example_compra = Compra(usuario_id=1, producto_id=1, total_productos=1)
