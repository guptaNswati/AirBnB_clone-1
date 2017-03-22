#!/usr/bin/python3
from models import *
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base]
from sqlalchemy.orm import relationship, backref
"""
"""


class User(BaseModel, Base):
    """
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship("Place", backref="user",
                          cascade="all, delete, delete-orphan"))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
