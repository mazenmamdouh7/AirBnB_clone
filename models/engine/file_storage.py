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

    def all(self):
        """Returns the dictionary __objects"""
        return slef.__objects

    def new(self, obj):                                                                                                                                             """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        obj_dict = {key : obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as jsonf:
            json.dump(obj_dict, jsonf)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as jsonf:
                obj_dict = json.load(jsonf)
            for key, value in obj_dict.items():
                self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
