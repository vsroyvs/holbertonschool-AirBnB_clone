#!/usr/bin/python3
import json
import unittest
from os import path
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unittest to FileStorage class"""

    def test_FileStorage(self):
        filestore1 = FileStorage()
        self.assertIsInstance(filestore1, FileStorage)
        basemodel1 = BaseModel()
        from models import storage
        self.assertIsInstance(storage, FileStorage)

    def test__file_path(self):
        filestore1 = FileStorage()
        self.assertIsNotNone(filestore1.FileStorage__file_path)

    def test__objects(self):
        filestore1 = FileStorage()
        self.assertIsNotNone(filestore1.FileStorage__objects)


if __name__ == '__main__':
    unittest.main()
