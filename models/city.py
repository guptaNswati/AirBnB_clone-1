#!/usr/bin/python3
from models import *
from sqlalchemy import Column, Integer, String, ForeignKey
import os
from models.base_model import BaseModel, Base
"""
This is the City class module. This module creates a City class that inherits
from BaseModel.
"""


class City(BaseModel, Base):
    """  This is the City class and it inherts from BaseModel """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """ Initiate City object """
        super().__init__(*args, **kwargs)
