from sqlalchemy import Table, Column, String, Boolean, Integer, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from utils.database import Database

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

    adresses = relationship('Adress', lazy='subquery')


class Collector(base):

    __tablename__ = 'collectors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    adress = relationship("Adress", uselist=False,
                          back_populates="collector", lazy='subquery')


class Adress(base):

    __tablename__ = 'adresses'

    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'))
    id_collector = Column(Integer, ForeignKey('collectors.id'))
    street = Column(String)
    number = Column(Integer)
    cep = cep = Column(String)
    district = district = Column(String)
    city = city = Column(String)
    state = state = Column(String)
    country = country = Column(String)

    collector = relationship(
        'Collector', back_populates="adress", lazy='subquery')

    def __repr__(self):
        return f'{self.street}, {self.number}. CEP {self.cep}, {self.district}, {self.city}, {self.state}, {self.country}'


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


class Partner(base):

    __tablename__ = 'partners'

    id = Column(Integer, primary_key=True)
    cnpj = Column(String)
    name = Column(String)
    points = Column(Integer, default=0)

    products = relationship('Product', lazy='subquery')


class Product(base):

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    id_partner = Column(Integer, ForeignKey('partners.id'))
    name = Column(String)
    price = Column(Integer)
    product_picture = Column(String)

    partner = relationship(
        'Partner', lazy='subquery')


class Request(base):

    __tablename__ = 'requests'

    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'))
    id_driver = Column(Integer, ForeignKey('drivers.id'))
    id_collector = Column(Integer, ForeignKey('collectors.id'))
    status = Column(String)
    points = Column(Integer, default=0)
    weight = Column(Integer)

    user = relationship(
        'User', lazy='subquery')
    driver = relationship(
        'Driver', lazy='subquery')
    collector = relationship(
        'Collector', lazy='subquery')


class History(base):

    __tablename__ = 'history'

    id = Column(Integer, primary_key=True)
    id_request = Column(Integer, ForeignKey('requests.id'))
    old_status = Column(String)
    new_status = Column(String)
    timestamp = Column(String)

    request = relationship(
        'Request', lazy='subquery')


class Order(base):

    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'))
    id_product = Column(Integer, ForeignKey('products.id'))
    timestamp = Column(String)

    user = relationship(
        'User', lazy='subquery')
    product = relationship(
        'Product', lazy='subquery')
