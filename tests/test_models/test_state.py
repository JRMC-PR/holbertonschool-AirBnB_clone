#!/usr/bin/python3


import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    def setUp(self):
        """Set up for the tests"""
        self.my_state = State()
        self.my_state.name = "California"

    def test_attributes(self):
        """Test the attributes of State"""
        self.assertEqual(self.my_state.name, "California")

    def test_inheritance(self):
        """Test if State inherits from BaseModel"""
        self.assertTrue(issubclass(type(self.my_state), BaseModel))

    def test_str(self):
        """Test the __str__ method"""
        self.assertEqual(str(self.my_state), "[State] ({}) {}".
                         format(self.my_state.id, self.my_state.__dict__))


if __name__ == '__main__':
    unittest.main()
