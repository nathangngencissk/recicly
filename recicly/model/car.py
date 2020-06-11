from sqlalchemy import Table, Column, String, Boolean, Integer, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from utils.database import Database
from model.driver import Driver


base = declarative_base()


class Car(base):

    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    id_driver = Column(Integer, ForeignKey('Driver.id'))
    brand = Column(String)
    model = Column(String)
    color = Column(String)

    driver = relationship('Driver', back_populates='cars')
