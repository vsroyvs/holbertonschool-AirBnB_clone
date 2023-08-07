#!/usr/bin/python3
"""Module FileStorage"""
import json
from os import path
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Public instance method that return all the dictionary"""
        return self.__objects

    def new(self, obj):
        """Public instance method that sets in dictionary the obj
        Args:
            obj (BaseModel or subclass):
        """
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """method to serialize: dicttionary to Json"""
        dic_store = {}
        for key, value in self.__objects.items():
            dic_store[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(dic_store))

    def reload(self):
        """method to deserialize"""
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                store_json = json.loads(file.read())
                for key, value in store_json.items():
                    value = store_json[key]
                    obj = eval(value['__class__'])(**value)
                    self.__objects[key] = obj
        else:
            pass
