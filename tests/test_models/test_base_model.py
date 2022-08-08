#!/usr/bin/python3
""" Performs testing on the components defined in the base_model.py file """


import unittest
from ...models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    """ A test class that inherits TestCase from unittest to perform testing """
    
    def test__init__(self):
        """ Tests if the __init__ works """
        my_model = BaseModel()
        self.assertIsNotNone(my_model)
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertIsNotNone(my_new_model)
        self.assertEqual(my_new_model.id, my_model.id)

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
