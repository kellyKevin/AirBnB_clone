#!/usr/bin/python3
"""
Unittest for Amenity Class
"""

import unittest
from datetime import datetime

from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def setUp(self):
        """
        Simple set up method.
        """
        self.amenity1 = Amenity()
        self.amenity2 = Amenity()

    def tearDown(self):
        """
        Simple tear down method.
        """
        del self.amenity1
        del self.amenity2

    def test_inheritance(self):
        """
        Test if Amenity class inherits from BaseModel.
        """
        self.assertIsInstance(self.amenity1, BaseModel)

    def test_attributes(self):
        """
        Test if Amenity class contains the attribute name.
        """
        self.assertTrue(hasattr(Amenity, "name"))

    def test_name_initialization(self):
        """
        Test if the name attribute is initialized as an empty string.
        """
        self.assertEqual(self.amenity1.name, "")

    def test_name_assignment(self):
        """
        Test if the name attribute can be assigned a value.
        """
        self.amenity1.name = "Pool"
        self.assertEqual(self.amenity1.name, "Pool")

    def test_type_attributes(self):
        """
        Test the type of Amenity class attributes.
        """
        self.assertEqual(type(self.amenity1.name), str)

    def test_str(self):
        """
        Test the str method.
        """
        self.assertEqual(
            str(self.amenity1),
            "[{}] ({}) {}".format(
                self.amenity1._class.name_,
                self.amenity1.id,
                self.amenity1._dict_,
            ),
        )

    def test_save(self):
        """
        Test the save method.
        """
        old_updated_at = self.amenity1.updated_at
        self.amenity1.save()
        self.assertNotEqual(old_updated_at, self.amenity1.updated_at)
        self.assertTrue(isinstance(self.amenity1.updated_at, datetime))

    def test_to_dict(self):
        """
        Test the to_dict method.
        """
        amenity_dict = self.amenity1.to_dict()
        self.assertEqual(amenity_dict["_class_"], "Amenity")
        self.assertEqual(type(amenity_dict["created_at"]), str)
        self.assertEqual(type(amenity_dict["updated_at"]), str)


if _name_ == "_main_":
    unittest.main()
