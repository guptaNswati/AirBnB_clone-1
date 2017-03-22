#!/usr/bin/python3
from models import *
from sqlalchemy import Column, Integer, String, ForeignKey
"""
This is the BaseModel module. This module defines a BaseModule class.
The BaseModule class defines common attributes/methods for other classes.
"""


class Amenity(BaseModel, Base):
    """ This is the Amenity Class, it inherts from BaseModel """
    if os.environ['HBNB_TYPE_STORAGE'] == 'db':
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ Initiate Amenity object """
        super().__init__(*args, **kwargs)
