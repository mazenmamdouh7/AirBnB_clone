#/usr/bin/pyhton3
import json
from models.base_model import BaseModel

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        obj_dict = {
            key: obj.to_dict()
            for key, obj in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as jsonf:
            json.dump(obj_dict, jsonf)

    def reload(self):
        """Deserializes the JSON file to __objects if it exists."""
        try:
            with open(FileStorage.__file_path, "r") as jsonf:
                obj_dict = json.load(jsonf)
                for key, value in obj_dict.items():
                    cls_name = value['__class__']
                    if cls_name == 'BaseModel':
                        FileStorage.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
