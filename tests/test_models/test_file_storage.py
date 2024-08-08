#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.storage.reload()

    def test_file_path(self):
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects_type(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        bm = BaseModel()
        self.storage.new(bm)
        self.assertIn(f"BaseModel.{bm.id}", self.storage.all())

    def test_save(self):
        bm = BaseModel()
        self.storage.new(bm)
        self.storage.save()
        self.assertTrue(os.path.isfile(self.storage._FileStorage__file_path))

    def test_reload(self):
        bm = BaseModel()
        self.storage.new(bm)
        self.storage.save()
        self.storage.reload()
        self.assertIn(f"BaseModel.{bm.id}", self.storage.all())

    def tearDown(self):
        """Clean up after each test."""
        try:
            os.remove(self.storage._FileStorage__file_path)
        except Exception:
            pass

if __name__ == "__main__":
    unittest.main()
