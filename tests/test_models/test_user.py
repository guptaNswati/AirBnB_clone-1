import unittest
from datetime import datetime
from models import *


class Test_UserModel(unittest.TestCase):
    """
    Test the user model class
    """

    def setUp(self):
        model = User()
        self.assertTrue(hasattr(model, "email"))
        self.assertTrue(hasattr(model, "password"))
        self.assertTrue(hasattr(model, "first_name"))
        self.assertTrue(hasattr(model, "last_name"))
        self.assertEqual(model.email, "")
        self.assertEqual(model.password, "")
        self.assertEqual(model.first_name, "")
        self.assertEqual(model.last_name, "")


if __name__ == "__main__":
    unittest.main()
