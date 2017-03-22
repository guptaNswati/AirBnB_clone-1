#!/usr/bin/python3
from models import *
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
"""
This is the Review class module. This module creates a Review class that
inherits from BaseModel.
"""


class Review(BaseModel, Base):
    """ This is the Review class and it inherts from BaseModel class """
    __tablename__ = "reviews"
    place_id = Column(String(60), nullable=False, Foreignkey('places.id'))
    user_id = Column(String(60), nullable=False, Foreignkey('users.id'))
    text = Column(String(1024), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
