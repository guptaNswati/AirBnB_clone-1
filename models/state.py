#!/usr/bin/python3
from models import *
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
import os
from models.base_model import BaseModel, Base
"""
This is the State class module. This module creates a State class that inherits
from BaseModel.
"""


class State(BaseModel, Base):
    """ This is the State Class and it inherts from BaseModel """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ Initiate a State object """
        super(State, self).__init__(*args, **kwargs)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        def cities(self):
            """ return the list of City objects from storage """
            city_list = storage.all("City")
            all_cities = []
            for city in city_list:
                if city.state_id == self.id:
                    all_cities.append(city)
            return all_cities
