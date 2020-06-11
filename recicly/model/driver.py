from sqlalchemy import Table, Column, String, Boolean, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base

from utils.database import Database
from model.person import Person


base = declarative_base()


class Driver(base):

    __tablename__ = 'drivers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    cpf = Column(String)
    email = Column(String)
    password = Column(String)
    drivers_license = Column(String)
    profile_picture = Column(String)
    points = Column(Integer, default=0)
