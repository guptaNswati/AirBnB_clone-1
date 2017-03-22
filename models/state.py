#!/usr/bin/python3
from models import *
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
"""
This is the State class module. This module creates a State class that inherits
from BaseModel.
"""


class State(BaseModel):
    """ This is the State Class and it inherts from BaseModel """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        super(State, self).__init__(*args, **kwargs)
