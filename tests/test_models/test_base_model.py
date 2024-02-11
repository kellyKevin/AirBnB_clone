#!/usr/bin/python3
"""
Test Module for BaseModel
"""
import os
import unittest
from datetime import datetime
from unittest.mock import patch

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def setUp(self):
        """
        Simple set up method.
        """
        self.base1 = BaseModel()
        self.base2 = BaseModel()

    def tearDown(self):
        """
        Simple tear down method.
        """
        del self.base1
        del self.base2

    def test_init(self):
        """
        Test the _init_ method.
        """
        self.assertTrue(isinstance(self.base1, BaseModel))

    def test_init_no_args(self):
        """
        Test _init_ with no arguments.
        """
        base = BaseModel()
        self.assertEqual(type(base.id), str)
        self.assertEqual(type(base.created_at), datetime)
        self.assertEqual(type(base.updated_at), datetime)
        self.assertEqual(base.created_at, base.updated_at)

    def test_init_with_kwargs(self):
        """
        Test _init_ with keyword arguments.
        """
        base = BaseModel(
            id="123",
            created_at="2022-01-01T00:00:00.000000",
            updated_at="2022-01-01T00:00:00.000000",
        )
        self.assertEqual(base.id, "123")
        self.assertEqual(base.created_at, datetime(2022, 1, 1))
        self.assertEqual(base.updated_at, datetime(2022, 1, 1))

    def test_init_with_wrong_time_format(self):
        """
        Test _init_ with wrong time format in keyword arguments.
        """
        with self.assertRaises(ValueError):
            BaseModel(
                created_at="2022-13-01T00:00:00.000000",
                updated_at="2022-13-01T00:00:00.000000",
            )

    def test_init_with_extra_attributes(self):
        """
        Test _init_ with extra attributes in keyword arguments.
        """
        base = BaseModel(attr1="value1", attr2="value2")
        self.assertEqual(base.attr1, "value1")
        self.assertEqual(base.attr2, "value2")

    @patch.object(FileStorage, "save")
    def test_save_calls_storage_save(self, mock_save):
        """
        Test that save method calls save method of storage.
        """
        bm = BaseModel()
        bm.save()
        mock_save.assert_called_once()

    @patch.object(FileStorage, "new")
    def test_new_instance_calls_storage_new(self, mock_new):
        """
        Test that _init_ method calls new method on
        storage if it’s a new instance.
        """
        bm = BaseModel()
        mock_new.assert_called_once_with(bm)

    @patch.object(FileStorage, "new")
    def test_existing_instance_does_not_call_storage_new(self, mock_new):
        """
        Test that _init_ method does not call new method on
        storage if it’s not a new instance.
        """
        bm = BaseModel(
            **{
                "id": "1234",
                "created_at": "2022-01-01T12:00:00.000000",
                "updated_at": "2022-01-01T12:00:00.000000",
            }
        )
        mock_new.assert_not_called()

    def test_attributes(self):
        """
        Test if BaseModel class contains the attribute id,
        created_at, updated_at.
        """
        self.assertTrue("id" in self.base1._dict_)
        self.assertTrue("created_at" in self.base1._dict_)
        self.assertTrue("updated_at" in self.base1._dict_)

    def test_type_attributes(self):
        """
        Test the type of BaseModel class attributes.
        """
        self.assertEqual(type(self.base1.id), str)
        self.assertEqual(type(self.base1.created_at), datetime)
        self.assertEqual(type(self.base1.updated_at), datetime)

    def test_unique_time_creation(self):
        """
        Test the uniqueness of time creation for each BaseModel instance.
        """
        self.assertNotEqual(self.base1.created_at, self.base2.created_at)

    def test_specific_id(self):
        """
        Test creating a BaseModel with a specific ID.
        """
        base3 = BaseModel()
        base3.id = "123"
        self.assertEqual(base3.id, "123")

    def test_string_representation(self):
        """
        Test the string representation of a BaseModel.
        """
        base_str = str(self.base1)
        expected_str = "[{}] ({}) {}".format(
            self.base1._class.name, self.base1.id, self.base1.dict_
        )
        self.assertEqual(base_str, expected_str)

    def test_save_to_file(self):
        """
        Test the save functionality that writes to a file.
        """
        self.base1.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_to_dict_return_type(self):
        """
        Test the return type of to_dict method.
        """
        base_dict = self.base1.to_dict()
        self.assertEqual(type(base_dict), dict)

    def test_dynamic_attributes(self):
        """
        Test the dynamic creation of attributes in dict.
        """
        self.base1.name = "Alx Africa"
        self.assertEqual(self.base1.name, "Alx Africa")

    def test_create_with_kwargs(self):
        """
        Test creating a BaseModel with kwargs.
        """
        base_dict = self.base1.to_dict()
        base2 = BaseModel(**base_dict)
        self.assertEqual(base2.to_dict(), base_dict)

    def test_create_without_args(self):
        """
        Test creating a BaseModel without args.
        """
        base3 = BaseModel()
        self.assertTrue(isinstance(base3, BaseModel))

    def test_wrong_time_format(self):
        """
        Test giving kwargs a wrong time format.
        """
        with self.assertRaises(ValueError):
            BaseModel(
                created_at="2022-13-01T15:38:32.089238",
                updated_at="2022-13-01T15:38:32.089238",
            )

    def test_str(self):
        """
        Test the str method.
        """
        self.assertEqual(
            str(self.base1),
            "[{}] ({}) {}".format(
                                self.base1._class.name_,
                                self.base1.id,
                                self.base1._dict_
                                ),
            )

    def test_save(self):
        """
        Test the save method.
        """
        old_updated_at = self.base1.updated_at
        self.base1.save()
        self.assertNotEqual(old_updated_at, self.base1.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method.
        """
        base_dict = self.base1.to_dict()
        self.assertEqual(type(base_dict), dict)
        self.assertEqual(base_dict["_class_"], "BaseModel")
        self.assertEqual(type(base_dict["created_at"]), str)
        self.assertEqual(type(base_dict["updated_at"]), str)
        self.assertEqual(base_dict["id"], self.base1.id)

    def test_unique_id(self):
        """
        Test if each BaseModel instance is assigned a unique id.
        """
        self.assertNotEqual(self.base1.id, self.base2.id)


if _name_ == "_main_":
    unittest.main()
