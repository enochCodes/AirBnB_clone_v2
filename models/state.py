#!/usr/bin/python3
""" State Module for HBNB project """

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """

    if models.storage_type == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref="state", cascade='all')
    else:
        name = ""

    if not models.storage_type == "db":
        @property
        def cities(self):
            """Getter"""
            return [v for v in models.storage.all(City).values()
                    if v.state_id == self.id]
