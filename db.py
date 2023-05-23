from databases import Database

from sqlalchemy import create_engine, MetaData, Column, Integer, String, Table
from data_env import user_value, password_value, host_value, port_value, database_value

SQLALCHEMY_DATABASE_URL = f'postgresql://{user_value}:{password_value}@{host_value}:{port_value}/{database_value}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
metadata = MetaData()

questions_db = Table(
    "questions_db",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("id_question", Integer, unique=True),
    Column("question", String),
    Column("answer", String),
    Column("data_created", String),
)

database = Database(SQLALCHEMY_DATABASE_URL)
