#!/usr/bin/python3
""" Base Model Module """
import uuid


class BaseModel:
    """ BaseModel Class """
    def __init__(self) -> None:
        self.id = str(uuid.uuid4())
