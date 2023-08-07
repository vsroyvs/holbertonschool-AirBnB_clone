#!/usr/bin/python3
"""Module for testing State class"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    def test_state(self):
        state1 = State()
        self.assertEqual(type(state1.name), str)
        self.assertIsNotNone(state1.name, "attribute is None")


if __name__ == '__main__':
    unittest.main()