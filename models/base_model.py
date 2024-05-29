#!/usr/bin/python3
""" Base Model Module """
import uuid
from datetime import datetime


class BaseModel:
    """ BaseModel Class """
    __date_iso_formated = datetime.now().isoformat()
    __date = datetime.now()

    def __init__(self) -> None:
        self.id = str(uuid.uuid4())
        self.created_at = self.__date
        self.updated_at = self.__date

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        self.updated_at = self.__date

    def to_dict(self):
        dict = self.__dict__
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.__date_iso_formated
        dict["updated_at"] = self.__date_iso_formated
        return dict
