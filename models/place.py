#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
# from models.review import Review
# from models.amenity import Amenity
import models


if models.storage_type == 'db':
    place_amenity = Table(
            'place_amenity', Base.metadata,
            Column(
                'place_id', String(60),
                ForeignKey('places.id'), nullable=False),
            Column(
                'amenity_id', String(60),
                ForeignKey('amenities.id'), nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    if models.storage_type == 'db':
        __tablename__ = 'places'

        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place', cascade='all')
        amenities = relationship(
            'Amenity', secondary=place_amenity, viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    if not models.storage_type == 'db':
        @property
        def reviews(self):
            """Reviews getter"""
            all_r = models.storage.all(Review).values()
            return [r for r in all_r if self.id == r.place_id]

        @property
        def amenities(self):
            """Amenities getter"""
            all_a = models.storage.all(Amenity).values()
            return [a for a in all_a if a.id in seld.amenity_ids]

        @amenities.setter
        def amenities(self, value):
            """Amenities setter"""
            if type(value) is Amenity:
                self.amenity_ids.append(value.id)
