#!/usr/bin/python3
""" a class user that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """child class of BaseModel that 
    update FileStorage class"""

    email = ""
    password = ""
    first_name =""
    last_name = ""
    