#!/usr/bin/python3
"""Module for test city class"""
import unittest
from models.base_model import BaseModel
from models.city import City

class TestCity(unittest.TestCase):
    def test_state_id(self):
        city1 = City()
        self.assertEqual(type(city1.state_id),str)
        self.assertIsNotNone(city1.state_id, "attribute is None")

    def test_name(self):
        city1 = City()
        self.assertEqual(type(city1.name),str)
        self.assertIsNotNone(city1.name, "attribute is None")


if __name__ == '__main__':
    unittest.main()
