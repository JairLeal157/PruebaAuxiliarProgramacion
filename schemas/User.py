from pydantic import BaseModel,Field;
from typing import Optional;
from werkzeug.security import generate_password_hash,check_password_hash
from models.Users import users as userTable
from config.connection import engine
#import Field


class User(BaseModel):
    id:int|None = Field(default=None, title="ID", description="ID del usuario")
    nombre:str  = Field(title="Nombre", description="Nombre del usuario", max_length=255)
    email:str  = Field(title="Email", description="Email del usuario", max_length=255)
    contraseña:str = Field(title="Contraseña", description="Contraseña del usuario", max_length=255)

    


example_user = User(nombre="Juan", email="Juan@email.com", contraseña="1234").dict()

def encriptar(contraseña): 
    return generate_password_hash(contraseña, method="sha256", salt_length=30)

def verificar(contraseña, hash): 
    return check_password_hash(hash, contraseña)

def existeUser(id:int):
    with engine.connect() as connection:
        result = connection.execute(userTable.select().where(userTable.c.id == id)).fetchall()
        if len(result) == 0: return False
    return True     