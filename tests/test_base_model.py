#!/usr/bin/python3
"""Unittest for class BaseModel."""

import unittest
from models.base_model import BaseModel
from time import sleep

class TestBaseModel(unittest.TestCase):
    """Class for testing methods."""
    def test_id(unittest.TestCase):
        """Method for testing id"""
        base_model_instance = BaseModel()
        self.assertEqual(len(base_model_instance.id), 36)
        self.assertTrue(isinstance(base_model_instance.id, str))

    def test_
