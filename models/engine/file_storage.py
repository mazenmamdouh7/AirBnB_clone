#!/usr/bin/python3
"""class FileStorage that serializes instances to a
JSON file and deserializes JSON file to instances.
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """class to save these objects to a file."""

    """Private class attributes"""
    __file_path = "file.json"
    __objects = {}


