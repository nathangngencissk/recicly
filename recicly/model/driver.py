from sqlalchemy import Table, Column, String, Boolean, Integer, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from utils.database import Database


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

    cars = relationship('Car', back_populates='driver', lazy='subquery')

    def __repr__(self):
        return f'{self.name}'

    def get_cars(self):
        cars = [car.__dict__ for car in self.cars]
        for car in cars:
            car.pop('_sa_instance_state', None)
        return cars


class Car(base):

    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    id_driver = Column(Integer, ForeignKey('drivers.id'))
    brand = Column(String)
    model = Column(String)
    color = Column(String)

    driver = relationship(Driver, back_populates='cars', lazy='subquery',
                          foreign_keys=[id_driver])

    def __repr__(self):
        return f'{self.brand} {self.model}'
