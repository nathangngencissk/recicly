import datetime

from sqlalchemy import Table, Column, String, Boolean, Integer, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from utils.database import Database
from utils import object_to_dict

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

    @classmethod
    def authenticate(cls, email, password):
        db = Database()
        result = db.query(
            f"SELECT * FROM users WHERE email = '{email}' AND password = '{password}'")

        return {
            'user': {} if len(result) == 0 else object_to_dict(User(**result[0])),
            'msg': 'User not found' if len(result) == 0 else 'User authenticated successfully'
        }

    def get_requests(self, *args, **kwargs):
        db = Database()
        result_set = db.query(
            f"SELECT * FROM requests WHERE id_user = {self.id}")
        requests = []
        for request in result_set:
            requests.append({
                'user': object_to_dict(self),
                'driver': db.get(Driver, request.id_driver, as_dict=True),
                'collector': db.get(Collector, request.id_collector, as_dict=True),
                'status': request.status,
                'points': request.points,
                'weight': request.weight
            })
        return requests

    def get_orders(self, *args, **kwargs):
        db = Database()
        result_set = db.query(
            f"SELECT * FROM orders WHERE id_user = {self.id}")
        orders = []
        for order in result_set:
            orders.append({
                'user': object_to_dict(self),
                'product': db.get(Product, order.id_product, as_dict=True),
                'timestamp': order.timestamp
            })
        return orders

    def exchange_points(self, product_id, *args, **kwargs):
        db = Database()
        product = db.get(Product, product_id)
        if self.points < product.price:
            return {
                'msg': 'Insufficient points'
            }
        self.points -= product.price
        db.update(self)
        order = Order(id_user=self.id, id_product=product.id,
                      timestamp=str(datetime.datetime.now().timestamp()))
        db.add(order)
        return {
            'msg': f'{product.name} bought successfully'
        }


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

    @classmethod
    def authenticate(cls, email, password):
        db = Database()
        result = db.query(
            f"SELECT * FROM drivers WHERE email = '{email}' AND password = '{password}'")

        return {
            'driver': {} if len(result) == 0 else object_to_dict(Driver(**result[0])),
            'msg': 'User not found' if len(result) == 0 else 'User authenticated successfully'
        }

    def get_requests(self, *args, **kwargs):
        db = Database()
        result_set = db.query(
            f"SELECT * FROM requests WHERE id_driver = {self.id}")
        requests = []
        for request in result_set:
            requests.append({
                'user': db.get(User, request.id_user, as_dict=True),
                'driver': object_to_dict(self),
                'collector': db.get(Collector, request.id_collector, as_dict=True),
                'status': request.status,
                'points': request.points,
                'weight': request.weight
            })
        return requests

    def exchange_points(self, points_quantity, *args, **kwargs):
        db = Database()
        if self.points < points_quantity:
            return {
                'msg': 'Insufficient points'
            }
        self.points -= points_quantity
        db.update(self)
        return {
            'msg': f'{points_quantity} exchanged successfully'
        }


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
