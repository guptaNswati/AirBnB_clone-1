#!/usr/bin/python3
import datetime
import uuid
import models
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
"""
This module contains
"""


Base = declarative_base()


class BaseModel:
    id = Column(String(60), primary_key=True, unique=True, nullable=False)
    created_at = Column(DateTime(), default=datetime.now(), nullable=False)
    updated_at = Column((DateTime(), default=datetime.now(), nullable=False)

    """The base class for all storage objects in this project"""
    def __init__(self, *args, **kwargs):
        """initialize class object"""
        if len(args) > 0:
            for k in args[0]:
                setattr(self, k, args[0][k])
        else:
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            self.id = str(uuid.uuid4())

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)


    def save(self):
        """method to update self"""
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """edit string representation"""
        return "[{}] ({}) {}".format(type(self)
                                     .__name__, self.id, self.__dict__)

    def to_json(self):
        """convert to json"""
        dupe = self.__dict__.copy()
        if '_sa_instance_state' in dupe:
            dupe.pop('_sa_instance_state')
        dupe["created_at"] = str(dupe["created_at"])
        if ("updated_at" in dupe):
            dupe["updated_at"] = str(dupe["updated_at"])
        dupe["__class__"] = type(self).__name__
        return dupe

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
