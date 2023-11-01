#!/usr/bin/python3
# & This module defines the class Review

# & Import the BaseModel class from the models.base_model module
from models.base_model import BaseModel


class Review(BaseModel):
    """This class defines a review by various attributes"""
    # & Define the attributes of the Review class
    place_id = ""  # & The ID of the place , init as an empty str
    user_id = ""  # & The ID of the user , init as an empty str
    text = ""  # & The text of the review, initialized as an empty string
