from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Float
from config.connection import meta, engine


products = Table(
    "products", meta, Column("id", Integer, primary_key=True, autoincrement=True), 
    Column("nombre", String(255)), 
    Column("precio", Float), 
    Column("url", String(255))
)

meta.create_all(engine)