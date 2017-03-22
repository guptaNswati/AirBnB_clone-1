#!/usr/bin/python3
from models import *
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
"""
This is the User module. This module defines a User class that inherits from
BaseModel.
"""


class User(BaseModel, Base):
    """ This is the User class and it inherts from BaseModel """
    if os.environ['HBNB_TYPE_STORAGE'] == 'db':
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship("Place", backref="user",
                              cascade="all, delete, delete-orphan")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """ Initiates User object """
        super().__init__(*args, **kwargs)
