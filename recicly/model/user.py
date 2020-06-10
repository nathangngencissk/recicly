from sqlalchemy import Table, Column, String, Boolean, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base

from utils.database import Database
from model.person import Person


base = declarative_base()


class User(base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    cpf = Column(String)
    email = Column(String)
    password = Column(String)
    admin = Column(Boolean, default=False)
    profile_picture = Column(String)
    points = Column(Integer, default=0)
