#!/usr/bin/python3
"""AirBnB clone - The console """
from datetime import datetime
from uuid import uuid4


class BaseModel():
    """Defines all common attributes/methods for`BaseModel`and its subclasses

    Attributes:
        id (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """
    def __init__(self, *args, **kwargs):
        """class constructor"""

        # self.created_at = datetime.strptime('created_at')
        # self.updated_at = datetime.strptime('updated_at')
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.id = str(uuid4())

    def __str__(self):
        """Returns the string representation of BaseModel."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, str(self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
