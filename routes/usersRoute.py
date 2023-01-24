from fastapi import APIRouter, Body, status, HTTPException
from schemas.User import User, example_user, encriptar, verificar, existeUser
from models.Users import users as userTable
from config.connection import engine


users = APIRouter(prefix="/users")

@users.get("/", response_model=list[User], status_code=status.HTTP_200_OK)
async def get_users():
    result = []
    with engine.connect() as connection:
        result = connection.execute(userTable.select()).fetchall()
        if len(result) == 0: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay usuarios")
    return result

@users.get("/{id}", status_code=status.HTTP_200_OK, response_model=User)
async def get_user(id:int):
    with engine.connect() as connection:
        result = connection.execute(userTable.select().where(userTable.c.id == id)).fetchall()
        if len(result) == 0: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe el usuario")
        result = result[0]
    return result

@users.post("/create", status_code=status.HTTP_201_CREATED, response_model=User)
async def create_users(user:User = Body(example=example_user)):
    with engine.connect() as connection:
        user.id = None
        user.contraseña = encriptar(user.contraseña);
        dict_user = user.dict()
        f = connection.execute(userTable.insert().values(dict_user))
        dict_user["id"] = f.lastrowid
    return dict_user

@users.put("/update/{id}/", status_code=status.HTTP_201_CREATED)
async def update_user(id:int, user:User = Body(example=example_user)):
    if not existeUser(id): raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe el usuario")
    with engine.connect() as connection:
        user.id = id
        user.contraseña = encriptar(user.contraseña);
        dict_user = user.dict()
        connection.execute(userTable.update().values(dict_user).where(userTable.c.id == id))
        print()
    return dict_user    


@users.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id:int):
    if not existeUser(id):
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe el usuario")
    with engine.connect() as connection:
        connection.execute(userTable.delete().where(userTable.c.id == id))
    return