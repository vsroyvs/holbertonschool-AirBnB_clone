#!/usr/bin/python3
"""Module for testing Review class"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    def test_place_id(self):
        review1 = Review()
        self.assertEqual(type(review1.place_id), str)
        self.assertIsNotNone(review1.place_id, "attribute is None")
    
    def test_user_id(self):
        review1 = Review()
        self.assertEqual(type(review1.user_id), str)
        self.assertIsNotNone(review1.user_id, "attribute is None")
    
    def test_text(self):
        review1 = Review()
        self.assertEqual(type(review1.text), str)
        self.assertIsNotNone(review1.text, "attribute is None")

if __name__ == '__main__':
    unittest.main()