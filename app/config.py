from decouple import config

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase

DB_HOST=config('DB_HOST')
DB_NAME=config('DB_NAME')
DB_USER=config('DB_USER')
DB_PASS=config('DB_PASS')
DB_PORT=config('DB_PORT')


DATABASE_URL =f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

session = sessionmaker(bind = engine)

class Base(DeclarativeBase):
    pass

