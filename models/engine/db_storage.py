#!/urs/bin/python3
"""db_storage module
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from ..base_model import Base
from ..user import User
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..place import Place
from ..review import Review


class DBStorage:
    """Class DBStorage"""

    __engine = None
    __session = None

    def __init__(self):
        """Instanciate new DBStorage"""
        db_user = os.getenv('HBNB_MYSQL_USER')
        db_pwd = os.getenv('HBNB_MYSQL_PWD')
        db_host = os.getenv('HBNB_MYSQL_HOST')
        db_name = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
                f"mysql+mysqldb://{db_user}:{db_pwd}@{db_host}/{db_name}",
                pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query all objects depending of the class name"""
        data = {}
        if cls:
            records = self.__session.query(cls).all()
            for rec in records:
                data[f'{rec.__class__.__name__}.{rec.id}'] = rec
        else:
            all_cls = {
                    "User": User,
                    "State": State,
                    "City": City,
                    "Amenity": Amenity,
                    "Place": Place,
                    "Review": Review
                    }
            for cl in all_cls:
                records = self.__session.query(all_cls[cl]).all()
                for rec in records:
                    if hasattr(rec, '_sa_instance_state'):
                        delattr(rec, '_sa_instance_state')
                    data[f'{rec.__class__.__name__}.{rec.id}'] = rec
        return data

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)()
