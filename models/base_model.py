#!/usr/bin/python3
""" Base Model Module """
import uuid
import datetime


class BaseModel:
    """ BaseModel Class """
    __date = datetime.datetime.now().isoformat()

    def __init__(self) -> None:
        self.id = str(uuid.uuid4())
        self.created_at = self.__date
        self.updated_at = self.__date

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        self.updated_at = self.__date

    def to_dict(self):
        return self.__dict__
