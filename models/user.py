#!/usr/bin/python3
# & This module defines the class User

# & Import the BaseModel class from the models.base_model module
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by various attributes"""
    # & Define the attributes of the User class
    email: str = ""  # & The email of the user, initialized as an empty string
    password: str = ""  # & The password of the user, initialized as an empty string
    first_name: str = ""  # & The first name of the user, init as an empty string
    last_name: str = ""  # & The last name of the user, init as an empty string
