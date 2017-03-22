#!/usr/bin/python3
from models import *
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import os
from models.base_model import BaseModel, Base
"""
This is the Place class module. This module creates a Place class that inherits
from BaseModel.
"""


class PlaceAmenity(Base):
    """ This is PlaceAmenity and it inherits from Base """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "place_amenity"
        place_id = Column(String(60), ForeignKey("places.id"),
                          primary_key=True, nullable=False)
        amenity_id = Column(String(60), ForeignKey("amenities.id"),
                            primary_key=True, nullable=False)


class Place(BaseModel, Base):
    """ This is the place class and it inherts from BaseModel """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=True)
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
        amenities = []

    def __init__(self, *args, **kwargs):
        """ Initiate Place object """
        super().__init__()
