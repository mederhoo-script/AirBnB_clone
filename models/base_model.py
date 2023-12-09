#!/usr/bin/python3
"""Define the BaseModel Class"""


import models
from uuid import uuid4
from datetime import datetime


class BaseModel:

    def __init__(self, *args, **kwargs):
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, t_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = dictionary['created_at'].isoformat()
        dictionary['updated_at'] = dictionary['updated_at'].isoformat()
        return dictionary

    def __str__(self):
        class_name = self.__class__.__name__
        return "[{:s}] ({:s}) {}".format(class_name, self.id, self.__dict__)