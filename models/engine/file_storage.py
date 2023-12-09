#!/usr/bin/python3
"""file storage that serialize instance to a JSON"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """file storage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        data = {}
        cls = {
            "BaseModel": BaseModel,
            "User": User
        }
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj_instance = cls[value["__class__"]](**value)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
