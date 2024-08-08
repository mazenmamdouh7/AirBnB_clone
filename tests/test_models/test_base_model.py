#!/usr/bin/python3
"""Unittest for FileStorage class."""

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage

class TestFileStorage(unittest.TestCase):
    """Class for testing the FileStorage class."""

    @classmethod
    def setUpClass(cls):
        """Set up class for FileStorage tests."""
        cls.storage = FileStorage()
        cls.file_path = cls.storage._FileStorage__file_path

    def setUp(self):
        """Setup for the proceeding tests."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test the all() method of FileStorage."""
        base_model = BaseModel()
        base_model.save()
        all_objects = self.storage.all()
        key = f"{base_model.__class__.__name__}.{base_model.id}"
        self.assertIn(key, all_objects)
        self.assertEqual(all_objects[key], base_model)

    def test_new(self):
        """Test the new() method of FileStorage."""
        base_model = BaseModel()
        self.storage.new(base_model)
        all_objects = self.storage.all()
        key = f"{base_model.__class__.__name__}.{base_model.id}"
        self.assertIn(key, all_objects)
        self.assertEqual(all_objects[key], base_model)

    def test_save(self):
        """Test the save() method of FileStorage."""
        base_model = BaseModel()
        base_model.save()
        self.storage.save()
        with open(self.file_path, 'r') as file:
            data = file.read()
        self.assertIn(f"{base_model.__class__.__name__}.{base_model.id}", data)

    def test_reload(self):
        """Test the reload() method of FileStorage."""
        base_model = BaseModel()
        base_model.save()
        self.storage.save()
        self.storage.reload()
        all_objects = self.storage.all()
        key = f"{base_model.__class__.__name__}.{base_model.id}"
        self.assertIn(key, all_objects)
        self.assertEqual(all_objects[key], base_model)

    def test_reload_no_file(self):
        """Test reload() when file does not exist."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

    @classmethod
    def tearDownClass(cls):
        """Clean up after tests."""
        if os.path.exists(cls.file_path):
            os.remove(cls.file_path)

if __name__ == "__main__":
    unittest.main()
