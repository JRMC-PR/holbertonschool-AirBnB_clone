#!/usr/bin/python3

import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.obj = BaseModel()
        self.obj.id = "123"

    def tearDown(self) -> None:
        """Tear down test environment"""
        return super().tearDown()

    def test_instantiation(self):
        """Test instantiation of FileStorage class"""
        self.assertIsInstance(self.storage, FileStorage)

    def test_Access(self):
        """Test r-w-x access to file"""
        self.assertTrue(os.access("models/engine/file_storage.py", os.R_OK))
        self.assertTrue(os.access("models/engine/file_storage.py", os.W_OK))
        self.assertFalse(os.access("models/engine/file_storage.py", os.X_OK))

    def test_all(self):
        """Test all method"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test new method"""
        self.storage.new(self.obj)
        key = self.obj.__class__.__name__ + "." + self.obj.id
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test save method"""
        self.storage.new(self.obj)
        self.storage.save()
        key = self.obj.__class__.__name__ + "." + self.obj.id
        with open(self.storage._FileStorage__file_path, "r") as f:
            self.assertIn(key, f.read())

    def test_reload(self):
        """Test reload method"""
        self.storage.new(self.obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = self.obj.__class__.__name__ + "." + self.obj.id
        self.assertIn(key, self.storage.all())

    def test_save_no_file(self):
        """Test save method when the file does not exist"""
        try:
            os.remove(self.storage._FileStorage__file_path)
        except FileNotFoundError:
            pass
        self.storage.new(self.obj)
        self.storage.save()
        key = self.obj.__class__.__name__ + "." + self.obj.id
        with open(self.storage._FileStorage__file_path, "r") as f:
            self.assertIn(key, f.read())

    def test_reload_invalid_json(self):
        """Test reload method with invalid JSON"""
        with open(self.storage._FileStorage__file_path, "w") as f:
            f.write("This is not valid JSON")
        with self.assertRaises(json.JSONDecodeError):
            self.storage.reload()

    def test_fundocs(self):
        """Test if funtions have documentation"""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)


if __name__ == '__main__':
    unittest.main()
