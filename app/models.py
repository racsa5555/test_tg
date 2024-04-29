from sqlalchemy import Column, Integer, String
from config import Base,engine

class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(Integer,primary_key=True)
    description = Column(String)

Base.metadata.create_all(bind = engine)