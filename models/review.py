#!/usr/bin/python3
from models import *
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import os
from models.base_model import BaseModel, Base
"""
This is the Review class module. This module creates a Review class that
inherits from BaseModel.
"""


class Review(BaseModel, Base):
    """ This is the Review class and it inherts from BaseModel class """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "reviews"
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """ Initiate Review object """
        super().__init__(*args, **kwargs)
