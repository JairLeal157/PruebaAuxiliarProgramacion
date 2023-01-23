from pydantic import BaseModel,Field;
from typing import Optional;
#import Field


class User(BaseModel):
    id:int|None = Field(default=None, title="ID", description="ID del usuario")
    nombre:str  = Field(title="Nombre", description="Nombre del usuario", max_length=255)
    email:str  = Field(title="Email", description="Email del usuario", max_length=255)
    contraseña:str = Field(title="Contraseña", description="Contraseña del usuario", max_length=255)


example_user = User(nombre="Juan", email="Juan@email.com", contraseña="1234").dict()
        