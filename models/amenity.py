#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
import models



class Amenity(BaseModel, Base):
    if models.storage_type == 'db':
        from models.place import place_amenity

        __tablename__ = 'amenities'

        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary=place_amenity)
    else:
        name = ""
