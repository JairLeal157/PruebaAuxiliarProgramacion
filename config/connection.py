from sqlalchemy import create_engine, MetaData

user = "root"
password = ""
host = "localhost"
port = "3306"
database = "basedatospruebaauxiliar"
string_connection = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(string_connection)
meta = MetaData()