#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Sets up testing environment"""
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def test_to_dict(self):
        """Tests to_dict method of BaseModel"""
        my_model_dict = self.my_model.to_dict()
        self.assertEqual(type(my_model_dict), dict)
        self.assertEqual(my_model_dict['name'], "My First Model")
        self.assertEqual(my_model_dict['my_number'], 89)
        self.assertEqual(my_model_dict['__class__'], "BaseModel")
        self.assertEqual(my_model_dict['created_at'], self.my_model.created_at.isoformat())
        self.assertEqual(my_model_dict['updated_at'], self.my_model.updated_at.isoformat())

    def test_save(self):
        """Tests save method of BaseModel"""
        old_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(old_updated_at, self.my_model.updated_at)

    def test_id(self):
        """Tests id attribute of BaseModel"""
        self.assertEqual(type(self.my_model.id), str)

    def test_created_at(self):
        """Tests created_at attribute of BaseModel"""
        self.assertEqual(type(self.my_model.created_at), datetime)

    def test_updated_at(self):
        """Tests updated_at attribute of BaseModel"""
        self.assertEqual(type(self.my_model.updated_at), datetime)

    if __name__ == '__main__':
        unittest.main()
