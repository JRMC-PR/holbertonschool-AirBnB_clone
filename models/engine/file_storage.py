#!/usr/bin/python3
"""This module defines the FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances"""
    # private Attributes
    __file_path = "file.json"  # path to the JSON file
    __objects = {}  # empty dictionary

    # Methods

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        temp_dict = {}

        for key, obj in self.__objects.items():
            temp_dict[key] = obj.to_dict()

        with open(self.__file_path, "w") as f:
            for key, obj in self.__objects.items():
                temp_dict[key] = obj.to_dict()
            json.dump(temp_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.loads(f.read())
                for key, obj in self.__objects.items():
                    self.__objects[key] = eval(obj["__class__"])(**obj)
        except FileNotFoundError:
            pass
