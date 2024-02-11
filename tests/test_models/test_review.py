#!/usr/bin/python3
"""
Unittest for Review Class
"""

import unittest
from datetime import datetime

from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    """

    def setUp(self):
        """
        Simple set up method.
        """
        self.review1 = Review()
        self.review2 = Review()

    def tearDown(self):
        """
        Simple tear down method.
        """
        del self.review1
        del self.review2

    def test_inheritance(self):
        """
        Test if Review class inherits from BaseModel.
        """
        self.assertIsInstance(self.review1, BaseModel)

    def test_attributes(self):
        """
        Test if Review class contains the attribute place_id, user_id, text.
        """
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertTrue(hasattr(Review, "user_id"))
        self.assertTrue(hasattr(Review, "text"))

    def test_attribute_initialization(self):
        """
        Test if the place_id, user_id, and text attributes are
        initialized as empty strings.
        """
        self.assertEqual(self.review1.place_id, "")
        self.assertEqual(self.review1.user_id, "")
        self.assertEqual(self.review1.text, "")

    def test_attribute_assignment(self):
        """
        Test if the place_id, user_id, and text attributes can
        be assigned values.
        """
        self.review1.place_id = "1234"
        self.review1.user_id = "5678"
        self.review1.text = "Great place!"
        self.assertEqual(self.review1.place_id, "1234")
        self.assertEqual(self.review1.user_id, "5678")
        self.assertEqual(self.review1.text, "Great place!")

    def test_type_attributes(self):
        """
        Test the type of Review class attributes.
        """
        self.assertEqual(type(self.review1.place_id), str)
        self.assertEqual(type(self.review1.user_id), str)
        self.assertEqual(type(self.review1.text), str)

    def test_str(self):
        """
        Test the str method.
        """
        self.assertEqual(
            str(self.review1),
            "[{}] ({}) {}".format(
                                self.review1._class.name_,
                                self.review1.id,
                                self.review1._dict_
                                ),
            )

    def test_save(self):
        """
        Test the save method.
        """
        old_updated_at = self.review1.updated_at
        self.review1.save()
        self.assertNotEqual(old_updated_at, self.review1.updated_at)
        self.assertTrue(isinstance(self.review1.updated_at, datetime))

    def test_to_dict(self):
        """
        Test the to_dict method.
        """
        review_dict = self.review1.to_dict()
        self.assertEqual(review_dict["_class_"], "Review")
        self.assertEqual(type(review_dict["created_at"]), str)
        self.assertEqual(type(review_dict["updated_at"]), str)


if _name_ == "_main_":
    unittest.main()
