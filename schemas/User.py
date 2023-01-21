from pydantic import BaseModel;
from typing import Optional;

class User(BaseModel):
    id:int|None = None
    nombre:str
    email:str
    contraseña:str