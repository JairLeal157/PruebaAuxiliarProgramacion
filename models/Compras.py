from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer
from config.connection import meta, engine

compras = Table(
    "compras", meta, Column("id", Integer, primary_key=True, autoincrement=True),
    Column("usuario_id", Integer),
    Column("producto_id", Integer),
    Column("total_productos", Integer)
)

meta.create_all(engine)