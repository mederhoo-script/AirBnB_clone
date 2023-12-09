#!/usr/bin/python3
""" BaseModel that define all common attribute/methods for other claseese"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """ parent class"""

    def __init__(self, *args, **kwargs):
        time_iso = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            # Assign each key-value pair from kwargs to instance attributes
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_iso)
                else:
                    self.__dict__[key] = value
        else:
            
            # Add the new instance to storage
            models.storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        # Call save(self) method of storage
        models.storage.save()

    def to_dict(self):
        # Create a copy of the instance's __dict__
        obj_dict = self.__dict__.copy()

        """Add the '__class__' key to the dictionary
        with the class name of the object"""
        obj_dict['__class__'] = self.__class__.__name__

        """Convert the 'created_at' attribute to a string
        in ISO format and add it to the dictionary"""
        obj_dict['created_at'] = self.created_at.isoformat()

        """Convert the 'updated_at' attribute to a string in
        ISO format and add it to the dictionary"""
        obj_dict['updated_at'] = self.updated_at.isoformat()

        # Return the resulting dictionary
        return obj_dict
    
    def __str__(self):
        class_name = self.__class__.__name__
        i_d = self.id
        dic = self.__dict__

        return "[{:s}] ({:s}) {}".format(class_name, i_d, dic)

