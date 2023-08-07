#!/usr/bin/python3
"""Module for testing Place class"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_city_id(self):
        place1 = Place()
        self.assertEqual(type(place1.city_id), str)
        self.assertIsNotNone(place1.city_id, "attribute is None")
    
    def test_user_id(self):
        place1 = Place()
        self.assertEqual(type(place1.user_id), str)
        self.assertIsNotNone(place1.user_id, "attribute is None")
    
    def test_name(self):
        place1 = Place()
        self.assertEqual(type(place1.name), str)
        self.assertIsNotNone(place1.name, "attribute is None")
    
    def test_description(self):
        place1 = Place()
        self.assertEqual(type(place1.description), str)
        self.assertIsNotNone(place1.description, "attribute is None")
    
    def test_number_rooms(self):
        place1 = Place()
        self.assertEqual(type(place1.number_rooms), int)
        self.assertIsNotNone(place1.number_rooms, "attribute is None")
    
    def test_number_bathrooms(self):
        place1 = Place()
        self.assertEqual(type(place1.number_bathrooms), int)
        self.assertIsNotNone(place1.number_bathrooms, "attribute is None")
    
    def test_max_guest(self):
        place1 = Place()
        self.assertEqual(type(place1.max_guest), int)
        self.assertIsNotNone(place1.max_guest, "attribute is None")

    def test_price_by_night(self):
        place1 = Place()
        self.assertEqual(type(place1.price_by_night), int)
        self.assertIsNotNone(place1.price_by_night, "attribute is None")
    
    def test_latitude(self):
        place1 = Place()
        self.assertEqual(type(place1.latitude), float)
        self.assertIsNotNone(place1.latitude, "attribute is None")

    def test_longitude(self):
        place1 = Place()
        self.assertEqual(type(place1.longitude), float)
        self.assertIsNotNone(place1.longitude, "attribute is None")

    def test_amenity_ids(self):
        place1 = Place()
        self.assertEqual(type(place1.amenity_ids), str)
        self.assertIsNotNone(place1.amenity_ids, "attribute is None")


if __name__ == '__main__':
    unittest.main()