from contextlib import contextmanager
import os

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.attributes import InstrumentedAttribute

from utils import object_to_dict


class Database():

    def __init__(self):
        self.database = 'recicly'
        self.user = 'recicly'
        self.password = os.getenv('PASSWORD')
        self.host = os.getenv('URL')
        self.port = '5432'

        db_string = f'postgres://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'
        self.db = create_engine(db_string)

    @contextmanager
    def connect(self):
        try:
            connection = self.db.connect()
            yield connection
        except Exception as exc:
            print(exc)
        finally:
            connection.close()

    @contextmanager
    def session(self):
        """Provide a transactional scope around a series of operations."""
        Session = sessionmaker(self.db)
        session = Session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def create_session(self):
        Session = sessionmaker(self.db)
        return Session()

    def get_all(self, table, as_dict=False):
        with self.session() as session:
            elements = [object_to_dict(result) for result in session.query(
                table)] if as_dict else [result for result in session.query(table)]
            session.expunge_all()
            return elements

    def get(self, table, id, as_dict=False):
        with self.session() as session:
            element = object_to_dict(session.query(table).get(
                id)) if as_dict else session.query(table).get(id)
            session.expunge_all()
            return element

    def add(self, element):
        with self.session() as session:
            session.add(element)
            session.commit()
            session.refresh(element)
            session.expunge_all()

    def update(self, element):
        table = type(element)
        with self.session() as session:
            updated_element = session.query(table).get(element.id)
            mapped_values = {}
            for attribute in element.__dict__:
                if attribute not in ['_sa_instance_state', 'id']:
                    mapped_values[attribute] = element.__dict__.get(
                        attribute)
            session.query(table).filter(
                table.id == element.id).update(mapped_values)
            session.commit()
            session.refresh(updated_element)
            session.expunge_all()
            return updated_element

    def delete(self, element):
        table = type(element)
        with self.session() as session:
            session.query(table).filter(table.id == element.id).delete(
                synchronize_session='evaluate')

    def query(self, table, query):
        with self.session() as session:
            elements = [object_to_dict(
                result) for result in session.query(table).filter(query)]
            session.expunge_all()
            return
