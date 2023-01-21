from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.connection import meta, engine


users = Table(
    "users", meta, Column("id", Integer, primary_key=True, autoincrement=True), 
    Column("nombre", String(255)), 
    Column("email", String(255)), 
    Column("contraseña", String(255))
)

meta.create_all(engine)