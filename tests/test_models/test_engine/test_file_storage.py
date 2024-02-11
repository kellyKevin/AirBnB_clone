#!/usr/bin/python3
"""
Module for testing FileStorage Engine
"""

import os
import unittest
from unittest.mock import patch

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def setUp(self):
        """
        Simple set up method.
        """
        self.storage = storage

    def tearDown(self):
        """
        Simple tear down method.
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        FileStorage.FileStorage_objects = {}

    def test_file_path_type(self):
        """
        Test the type of __file_path attribute.
        """
        self.assertEqual(type(self.storage.FileStorage_file_path), str)

    def test_file_path_value(self):
        """
        Test the value of __file_path attribute.
        """
        self.assertEqual(self.storage.FileStorage_file_path, "file.json")

    def test_objects_type(self):
        """
        Test the type of __objects attribute.
        """
        self.assertEqual(type(self.storage.FileStorage_objects), dict)

    def test_storage_instance_type(self):
        """
        Test the type of storage instance.
        """
        self.assertEqual(type(self.storage), FileStorage)

    def test_all_with_no_objects(self):
        """
        Test the all method with no objects in storage.
        """
        self.storage.FileStorage_objects = {}
        self.assertEqual(self.storage.all(), {})

    def test_new_with_none(self):
        """
        Test the new method with None as an argument.
        """
        self.storage.new(None)
        self.assertEqual(self.storage.all(), {})

    def test_save_with_no_objects(self):
        """
        Test the save method with no objects in storage.
        """
        self.storage.FileStorage_objects = {}
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload_with_no_file(self):
        """
        Test the reload method with no file.
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

    def test_reload_with_empty_file(self):
        """
        Test the reload method with an empty file.
        """
        with open("file.json", "w") as f:
            pass
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

    def test_storage_instance(self):
        """
        Test that storage is an instance of FileStorage.
        """
        self.assertIsInstance(storage, FileStorage)

    @patch.object(FileStorage, "reload")
    def test_reload_called_on_storage(self, mock_reload):
        """
        Test that reload method is called on storage.
        """
        storage.reload()
        mock_reload.assert_called_once()

    def test_objects_changes(self):
        """
        Test if __objects changes when a new object is added.
        """
        initial_objects = self.storage.all().copy()
        instance = BaseModel()
        self.storage.new(instance)
        self.assertNotEqual(self.storage.all(), initial_objects)

    def test_objects_contents(self):
        """
        Test the contents of __objects.
        """
        instance = BaseModel()
        self.storage.new(instance)
        key = instance._class.name_ + "." + instance.id
        self.assertTrue(key in self.storage.all())

    def test_all(self):
        """
        Test the all method.
        """
        self.assertEqual(type(self.storage.all()), dict)

    def test_new(self):
        """
        Test the new method.
        """
        for class_name in [
                            BaseModel,
                            User,
                            State,
                            City,
                            Amenity,
                            Place,
                            Review
                            ]:
            instance = class_name()
            self.storage.new(instance)
            key = instance._class.name_ + "." + instance.id
            self.assertTrue(key in self.storage.all())

    def test_save_and_reload(self):
        """
        Test the save and reload methods.
        """
        for class_name in [
                            BaseModel,
                            User,
                            State,
                            City,
                            Amenity,
                            Place,
                            Review
                            ]:
            instance = class_name()
            self.storage.new(instance)
            self.storage.save()
            self.storage.reload()
            key = instance._class.name_ + "." + instance.id
            self.assertTrue(key in self.storage.all())
            self.assertTrue(os.path.exists("file.json"))


if _name_ == "_main_":
    unittest.main()
