#!/usr/bin/python3

""" Test module for FileStorage class """


import unittest
from datetime import datetime
from ....models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """ Class definition for FileStorage testing """


    def test_all(self):
        """ Tests the all function in Filestorage """


        store = FileStorage()
        all_obj = store.all()
        self.assertEqual(all_obj, {})

    def test_new(self):
        """ Tests the new function in FileStorage """
        

        store = FileStorage()
        store.new({'id': "23424232442dvdf2113g", 'created_at': datetime.now(), 'updated_at': datetime.now()})
        all_obj = store.all()
        self.assertNotEqual(all_obj, {})
