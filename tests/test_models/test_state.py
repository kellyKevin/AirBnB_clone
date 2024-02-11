#!/usr/bin/python3
"""
Unittest for State Class
"""

import unittest
from datetime import datetime

from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """

    def setUp(self):
        """
        Simple set up method.
        """
        self.state1 = State()
        self.state2 = State()

    def tearDown(self):
        """
        Simple tear down method.
        """
        del self.state1
        del self.state2

    def test_inheritance(self):
        """
        Test if State class inherits from BaseModel.
        """
        self.assertIsInstance(self.state1, BaseModel)

    def test_attributes(self):
        """
        Test if State class contains the attribute name.
        """
        self.assertTrue(hasattr(State, "name"))

    def test_attribute_initialization(self):
        """
        Test if the name attribute is initialized as an empty string.
        """
        self.assertEqual(self.state1.name, "")

    def test_attribute_assignment(self):
        """
        Test if the name attribute can be assigned a value.
        """
        self.state1.name = "Test State"
        self.assertEqual(self.state1.name, "Test State")

    def test_type_attributes(self):
        """
        Test the type of State class attributes.
        """
        self.assertEqual(type(self.state1.name), str)

    def test_str(self):
        """
        Test the str method.
        """
        self.assertEqual(
            str(self.state1),
            "[{}] ({}) {}".format(
                                self.state1._class.name_,
                                self.state1.id,
                                self.state1._dict_
                                ),
            )

    def test_save(self):
        """
        Test the save method.
        """
        old_updated_at = self.state1.updated_at
        self.state1.save()
        self.assertNotEqual(old_updated_at, self.state1.updated_at)
        self.assertTrue(isinstance(self.state1.updated_at, datetime))

    def test_to_dict(self):
        """
        Test the to_dict method.
        """
        state_dict = self.state1.to_dict()
        self.assertEqual(state_dict["_class_"], "State")
        self.assertEqual(type(state_dict["created_at"]), str)
        self.assertEqual(type(state_dict["updated_at"]), str)


if _name_ == "_main_":
    unittest.main()
