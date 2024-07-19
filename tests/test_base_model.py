#!/usr/bin/python3
"""Unittest for class BaseModel."""

import unittest
from models.base_model import BaseModel
from time import sleep

class TestBaseModel(unittest.TestCase):
    """Class for testing methods."""
    def test_id(self):
        """Method for testing id"""
        base_model_instance = BaseModel()
        self.assertEqual(len(base_model_instance.id), 36)
        self.assertTrue(isinstance(base_model_instance.id, str))

    def test_created_at(self):
        """Test for created at type."""
        base_model_instance = BaseModel()
        self.assertEqual(type(base_model_instance.created_at), datetime)

    def test_updated_at(self):
        """Test for updated at type."""
        base_model_instance = BaseModel()
        self.assertEqual(type(base_model_instance.updated_at), datetime)

    def test_save(self):
        """Test for save updated at"""
        base_model_instance = BaseModel()
        old_updated_at = base_model_instance.updated_at
        sleep(0.1)
        base_model_instance.save()
        self.assertNotEqual(base_model_instance.updated_at, old_updated_at)

    if __name__ == "__main__":
        unittest.main()
