#!/usr/bin/python3
"""AirBnB clone - The console """
from datetime import datetime
import uuid
import models


class BaseModel:
    """Defines all common attributes/methods for`BaseModel`and its subclasses

    Attributes:
        id (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    def __init__(self, *args, **kwargs):
        """This is a constructor of the class"""
        if kwargs:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at 
            models.storage.new(self)

    def __str__(self):
        """Returns the string representation of BaseModel."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        dict = self.__dict__.copy()
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        dict["__class__"] = self.__class__.__name__
        return dict
