#!/usr/bin/python3
"""
Unittest for City Class
"""

import unittest
from datetime import datetime

from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """

    def setUp(self):
        """
        Simple set up method.
        """
        self.city1 = City()
        self.city2 = City()

    def tearDown(self):
        """
        Simple tear down method.
        """
        del self.city1
        del self.city2

    def test_inheritance(self):
        """
        Test if City class inherits from BaseModel.
        """
        self.assertIsInstance(self.city1, BaseModel)

    def test_attributes(self):
        """
        Test if City class contains the attribute state_id and name.
        """
        self.assertTrue(hasattr(City, "state_id"))
        self.assertTrue(hasattr(City, "name"))

    def test_attribute_initialization(self):
        """
        Test if the state_id and name attributes are
        initialized as empty strings.
        """
        self.assertEqual(self.city1.state_id, "")
        self.assertEqual(self.city1.name, "")

    def test_attribute_assignment(self):
        """
        Test if the state_id and name attributes can be assigned values.
        """
        self.city1.state_id = "1234"
        self.city1.name = "Test City"
        self.assertEqual(self.city1.state_id, "1234")
        self.assertEqual(self.city1.name, "Test City")

    def test_type_attributes(self):
        """
        Test the type of City class attributes.
        """
        self.assertEqual(type(self.city1.state_id), str)
        self.assertEqual(type(self.city1.name), str)

    def test_str(self):
        """
        Test the str method.
        """
        self.assertEqual(
            str(self.city1),
            "[{}] ({}) {}".format(
                                self.city1._class.name_,
                                self.city1.id,
                                self.city1._dict_
                                ),
            )

    def test_save(self):
        """
        Test the save method.
        """
        old_updated_at = self.city1.updated_at
        self.city1.save()
        self.assertNotEqual(old_updated_at, self.city1.updated_at)
        self.assertTrue(isinstance(self.city1.updated_at, datetime))

    def test_to_dict(self):
        """
        Test the to_dict method.
        """
        city_dict = self.city1.to_dict()
        self.assertEqual(city_dict["_class_"], "City")
        self.assertEqual(type(city_dict["created_at"]), str)
        self.assertEqual(type(city_dict["updated_at"]), str)


if _name_ == "_main_":
    unittest.main()
