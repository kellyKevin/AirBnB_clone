#!/usr/bin/python3
"""
Unittest for User Class
"""

import unittest
from datetime import datetime

from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """

    def setUp(self):
        """
        Simple set up method.
        """
        self.user1 = User()
        self.user2 = User()

    def tearDown(self):
        """
        Simple tear down method.
        """
        del self.user1
        del self.user2

    def test_inheritance(self):
        """
        Test if User class inherits from BaseModel.
        """
        self.assertIsInstance(self.user1, BaseModel)

    def test_attributes(self):
        """
        Test if User class contains the attribute email,
        password, first_name, last_name.
        """
        self.assertTrue(hasattr(User, "email"))
        self.assertTrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))

    def test_attribute_initialization(self):
        """
        Test if the email, password, first_name, and last_name
        attributes are initialized as empty strings.
        """
        self.assertEqual(self.user1.email, "")
        self.assertEqual(self.user1.password, "")
        self.assertEqual(self.user1.first_name, "")
        self.assertEqual(self.user1.last_name, "")

    def test_attribute_assignment(self):
        """
        Test if the email, password, first_name, and last_name
        attributes can be assigned values.
        """
        self.user1.email = "test@example.com"
        self.user1.password = "password"
        self.user1.first_name = "Test"
        self.user1.last_name = "User"
        self.assertEqual(self.user1.email, "test@example.com")
        self.assertEqual(self.user1.password, "password")
        self.assertEqual(self.user1.first_name, "Test")
        self.assertEqual(self.user1.last_name, "User")

    def test_type_attributes(self):
        """
        Test the type of User class attributes.
        """
        self.assertEqual(type(self.user1.email), str)
        self.assertEqual(type(self.user1.password), str)
        self.assertEqual(type(self.user1.first_name), str)
        self.assertEqual(type(self.user1.last_name), str)

    def test_str(self):
        """
        Test the str method.
        """
        self.assertEqual(
            str(self.user1),
            "[{}] ({}) {}".format(
                                self.user1._class.name_,
                                self.user1.id,
                                self.user1._dict_
                                ),
            )

    def test_save(self):
        """
        Test the save method.
        """
        old_updated_at = self.user1.updated_at
        self.user1.save()
        self.assertNotEqual(old_updated_at, self.user1.updated_at)
        self.assertTrue(isinstance(self.user1.updated_at, datetime))

    def test_to_dict(self):
        """
        Test the to_dict method.
        """
        user_dict = self.user1.to_dict()
        self.assertEqual(user_dict["_class_"], "User")
        self.assertEqual(type(user_dict["created_at"]), str)
        self.assertEqual(type(user_dict["updated_at"]), str)


if _name_ == "_main_":
    unittest.main()
