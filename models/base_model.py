#!/usr/bin/python3
""" Base Model Module """
import uuid
from datetime import datetime


class BaseModel:
    """ BaseModel Class """

    def __init__(self) -> None:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict = self.__dict__
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = datetime.now().isoformat()
        dict["updated_at"] = datetime.now().isoformat()
        return dict
