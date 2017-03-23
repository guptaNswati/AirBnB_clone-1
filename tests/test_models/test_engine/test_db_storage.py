import unittest
import os
import os.path
from datetime import datetime
from models.engine.db_storage import DBStorage
from models import *
from models.base_model import Base
"""
This module contains db storage test objects.
"""


class Test_DBStorage(unittest.TestCase):
    """
    Test the file storage class
    """

    def setUp(self):
        self.store = DBStorage()

        test_args = {'updated_at': datetime(2017, 2, 12, 00, 31, 53, 331997),
                     'id': 'f519fb40-1f5c-458b-945c-2ee8eaaf4900',
                     'created_at': datetime(2017, 2, 12, 00, 31, 53, 331900)}
        self.model = State(**test_args)
        self.test_len = 0

    def test_all(self):
        self.assertEqual(len(self.store.all('State')), self.test_len)

    def test_new(self):
        self.test_len = len(self.store.all())
        self.assertEqual(len(self.store.all()), self.test_len)
        self.model.save()
        self.assertEqual(len(self.store.all()), self.test_len + 1)
        a = State()
        a.save()
        self.assertEqual(len(self.store.all()), self.test_len + 2)

    def test_save(self):
        self.test_len = len(self.store.all())
        a = State()
        a.save()
        self.assertEqual(len(self.store.all()), self.test_len + 1)
        b = User()
        self.assertNotEqual(len(self.store.all()), self.test_len + 2)
        b.save()
        self.assertEqual(len(self.store.all()), self.test_len + 2)


if __name__ == "__main__":
    unittest.main()
