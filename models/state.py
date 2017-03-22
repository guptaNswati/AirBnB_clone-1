#!/usr/bin/python3
from models import *
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base]
from sqlalchemy.orm import relationship, backref
"""
"""


class State(BaseModel):
    """
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        super(State, self).__init__(*args, **kwargs)
