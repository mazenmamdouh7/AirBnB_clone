#!/usr/bin/python3
"""
This file define BaseModel that defines all
common attributes/methods for other classes
"""

from uuid import uuid4

class BaseModel:
    """Base class for all our classes."""
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        className = self.__class__.__name__
        return f"[{className}] (self.id) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.utcnow()

    def to_dict(self, **kwargs):
