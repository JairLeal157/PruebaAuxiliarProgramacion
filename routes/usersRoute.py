from fastapi import APIRouter
from schemas.User import User
from models.Users import users as userTable
from config.connection import engine
from werkzeug.security import generate_password_hash,check_password_hash


users = APIRouter(prefix="/users")
encriptar = lambda contraseña: generate_password_hash(contraseña, method="sha256", salt_length=30)
verificar = lambda contraseña, hash: check_password_hash(hash, contraseña)

@users.get("/")
async def get_users():
    with engine.connect() as connection:
        result = connection.execute(userTable.select()).fetchall()
    return result

@users.get("/{id}")
async def get_user(id:int):
    with engine.connect() as connection:
        result = connection.execute(userTable.select().where(userTable.c.id == id)).fetchall()[0]
    return result

@users.post("/create", response_model= User)
async def create_users(user:User):
    with engine.connect() as connection:
        user.id = None
        user.contraseña = encriptar(user.contraseña);
        dict_user = user.dict()
        connection.execute(userTable.insert().values(dict_user))
    return user

@users.put("/update/")
async def update_user(user:User):
    with engine.connect() as connection:
        user.contraseña = encriptar(user.contraseña);
        dict_user = user.dict()
        connection.execute(userTable.update().values(dict_user).where(userTable.c.id == user.id))
    return


@users.delete("/delete/{id}")
async def delete_user(id:int):
    with engine.connect() as connection:
        connection.execute(userTable.delete().where(userTable.c.id == id))
    return