#!/usr/bin/python3
""" City Module for HBNB project """

from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base

import models


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    

    if models.storage_type == 'db':
        __tablename__ = "cities"

        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
    else:
        state_id = ""
        name = ""
