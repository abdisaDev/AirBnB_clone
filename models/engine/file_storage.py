#!/usr/bin/python3
""" Files Storage Module """
import json
import os


class FileStorage:
    """ File Storage Class """
    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj
        print(self.__objects)

    def save(self):
        print(FileStorage.__objects)
        with open(FileStorage.__file_path, "w") as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        deserialized = None

        if not os.path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as file:
            try:
                json.load(file)
            except json.JSONDecodeError:
                pass

        if deserialized is None:
            return
