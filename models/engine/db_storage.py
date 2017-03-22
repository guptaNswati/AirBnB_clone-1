#!/usr/bin/python3
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *


"""
This module contains datastorage engine called DBStorage, which creates the
database and session.
"""


os.environ['HBNB_MYSQL_HOST'] = 'localhost'


class DBStorage:
    __engine = None
    __session = None
    class_dict = {'User': User,
                  'State': State, 'City': City,
                  'Amenity': Amenity, 'Place': Place,
                  'Review': Review}

    def __init__(self):
        """
        create the engine and link to mysql database
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.environ['HBNB_MYSQL_USER'], os.environ['HBNB_MYSQL_PWD'],
            os.environ['HBNB_MYSQL_HOST'], os.environ['HBNB_MYSQL_DB']))
        if os.environ['HBNB_MYSQL_ENV'] == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session all objects
        """
        value_dic = {}
        if cls is not None:
            for objc in self.__session.query(self.class_dict[cls]):
                value_dic[objc.id] = objc
        else:
            for clas in class_dict:
                for objc in self.__session.query(self.class_dict[clas]):
                    if (objc):
                        value_dic[objc.id] = objc
        return value_dic

    def new(self, obj):
        """
        add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database and create the current
        database session
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
