#!/usr/bin/python3
"""
This file define BaseModel that defines all
common attributes/methods for other classes
"""


from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """Base class for all our classes."""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""
        className = self.__class__.__name__
        return f"[{className}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self, **kwargs):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
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
