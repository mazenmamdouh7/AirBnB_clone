#!/usr/bin/python3
"""Unittest for class BaseModel."""

import unittest
from models.base_model import *
from time import sleep
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Class for testing methods."""
    def setUp(self):
        """ setup for the proceeding tests """
        self.model = BaseModel()
        self.model.name = "My First Model"
        self.model.my_number = 89

    def test_init(self):
        """Ensure all instace is not none"""
        base_model_instance = BaseModel()
        self.assertIsNotNone(base_model_instance.id)
        self.assertIsNotNone(base_model_instance.created_at)
        self.assertIsNotNone(base_model_instance.updated_at)

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
        """Test for save updated at."""
        base_model_instance = BaseModel()
        old_updated_at = base_model_instance.updated_at
        sleep(0.1)
        base_model_instance.save()
        self.assertNotEqual(base_model_instance.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test for dict containing correct keys"""
        base_model_instance = BaseModel()
        model_dict = base_model_instance.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], base_model_instance.id)
        self.assertEqual(model_dict['created_at'], base_model_instance.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], base_model_instance.updated_at.isoformat())

    def test_str(self):
        """Test for str return correct values"""
        base_model_instance = BaseModel()
        expected = f"[BaseModel] ({base_model_instance.id}) {base_model_instance.__dict__}"
        self.assertEqual(str(base_model_instance), expected)

if __name__ == "__main__":
    unittest.main()
