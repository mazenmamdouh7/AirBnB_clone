#!/usr/bin/python3
"""
This file define BaseModel that defines all
common attributes/methods for other classes
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base class for all our classes."""
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def __str__(self):
        className = self.__class__.__name__
        return f"[{className}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.utcnow()

    def to_dict(self, **kwargs):
        dict_representation = self.__dict__.copy()
        dict_representation['__class__'] = self.__class__.__name__
        dict_representation['created_at'] = self.created_at.isoformat()
        dict_representation['updated_at'] = self.updated_at.isoformat()
        return dict_representation

    if __name__ == "__main__":
        base_model_instance = BaseModel()
        print(base_model_instance)
        base_model_instance.save()
        print(base_model_instance.to_dict())
