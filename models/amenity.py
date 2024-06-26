#!/usr/bin/python3
""" State Module for HBNB project """
from sqlachemy import Column, String

from models.base_model import BaseModel, Base
import models


class Amenity(BaseModel, Base):
    if models.storage_type == 'db':
        __tablename__ = 'amenities'

        name = Column(String(128), nullable=False)
        place_amenities = 
    else:
        name = ""
