#!/usr/bin/python3
"""script to to create a unique
FileStorage instance for your application"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
