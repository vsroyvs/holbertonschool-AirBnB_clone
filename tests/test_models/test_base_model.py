#!/usr/bin/python3
"""Module for test BaseModel class"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test for BaseModel class"""

    def initial_test(self):
        """"testing initial"""
        object = BaseModel()
        self.assertIsInstance(object.id, str)

    def test__str__method(self):
        """testing __str__ method"""
        object = BaseModel()
        expected_str = f"BaseModel(id={object.id})"
        self.assertNotEqual(str(object), expected_str)

    def test_uuid(self):
        """testing differents uuid"""
        model = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model.id, model_2.id)

    def test_datetime_model(self):
        """testing datetime base model"""
        object_1 = BaseModel()
        object_2 = BaseModel()
        self.assertNotEqual(object_1.created_at, object_1.updated_at)
        self.assertNotEqual(object_1.created_at, object_2.created_at)

    def test_save(self):
        """check if it updates correctly after calling the save method"""
        obj = BaseModel()
        prev_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(prev_updated_at, obj.updated_at)

    def test_dict(self):
        """testing to_dict method"""
        object = BaseModel()
        full_dict = object.to_dict()
        self.assertNotEqual(full_dict, self.__dict__)


if __name__ == '__main__':
    unittest.main()
