#!/usr/bin/python3
""" Performs testing on the components defined in the base_model.py file """


import unittest
from ...models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    """ A test class that inherits TestCase from unittest to perform testing """
    def test_save(self):
        """ Function that test the save instance method in BaseModel class """
        model = BaseModel()
        model.save()
        self.assertNotEqual(model.updated_at, model.created_at)

    def test_to_dict(self):
        """ Tests the to_dict method in BaseModel class """
        model = BaseModel()
        dic = model.to_dict()
        self.assertEqual(type(dic), dict)
