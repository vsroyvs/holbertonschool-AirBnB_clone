#!/usr/bin/python3
"""Module for test User class"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test for User class"""

    def test_email(self):
        user1 = User()
        self.assertEqual(type(user1.email), str)
        self.assertIsNotNone(user1.email, "attribute is None")

    def test_password(self):
        user1 = User()
        self.assertEqual(type(user1.password), str)
        self.assertIsNotNone(user1.password, "attribute is None")

    def test_first_name(self):
        user1 = User()
        self.assertEqual(type(user1.first_name), str)
        self.assertIsNotNone(user1.password, "attribute is None")

    def test_last_name(self):
        user1 = User()
        self.assertEqual(type(user1.last_name), str)
        self.assertIsNotNone(user1.last_name, "attribute is None")

if __name__ == '__main__':
    unittest.main()