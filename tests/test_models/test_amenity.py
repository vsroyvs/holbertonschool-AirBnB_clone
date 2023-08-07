#!/usr/bin/python3
"""Module for test amenity class"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_name(self):
        amenity1 = Amenity()
        self.assertEqual(type(amenity1.name),str)
        self.assertIsNotNone(amenity1.name, "attribute is None")


if __name__ == '__main__':
    unittest.main()