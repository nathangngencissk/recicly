from sqlalchemy import Table, Column, String, Boolean, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base

from utils.database import Database
from model.person import Person


base = declarative_base()


class Collector(base):

    __tablename__ = 'collectors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
