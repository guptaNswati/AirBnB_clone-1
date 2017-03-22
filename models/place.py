#!/usr/bin/python3
from models import *
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
"""
This is the Place class module. This module creates a Place class that inherits
from BaseModel.
"""


class PlaceAmenity(Base):
    """ This is PlaceAmenity and it inherits from Base """
    __tablename__ = "place_amenity"
    place_id = Column(String(60), primary_key=True, nullable=False,
                      ForeignKey("places.id"))
    amenity_id = Column(String(60), primary_key=True, nullable=False,
                        ForeignKey("amenities.id"))


class Place(BaseModel, Base):
    """ This is the place class and it inherts from BaseModel """
    __tablename__ = "places"
    city_id = Column(String(60), nullable=False, ForeignKey("cities.id"))
    user_id = Column(String(60), nullable=False, ForeignKey("users.id"))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=True)

    def __init__(self, *args, **kwargs):
        super().__init__()
