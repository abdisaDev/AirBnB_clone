#!/usr/bin/python3
""" Initalaize Models Package """
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()