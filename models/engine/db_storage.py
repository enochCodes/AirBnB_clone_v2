#!/urs/bin/python3
"""db_storage module
"""

import os
from sqlalchemy import create_engine


class DBStorage:
    """Class DBStorage"""

    __engine = None
    __session = None

    def __init__(self):
        """Instanciate new DBStorage"""
        db_user = os.environ.get('HBNB_MYSQL_USER')
        db_pwd = os.environ.get('HBNB_MYSQL_PWD')
        db_host = os.environ.get('HBNB_MYSQL_HOST')
        db_name = os.environ.get('HBNB_MYSQL_DB')
        self.__engine = create_engine(
                "mysql+mysqldb://{db_user}:{db_pwd}@{db_host}/{db_name}"
                pool_pre_ping=True)

    def all(self, cls=None):
        """query all objects depending of the class name"""
        pass

    def new(self, obj):
        """add the object to the current database session"""
        pass

    def save(self):
        """commit all changes of the current database session"""
        pass

    def delete(self, obj=None):
        """delete from the current database session"""
        pass

    def reload(self):
        """create all tables in the database"""
        pass
