import unittest
from datetime import datetime
from models import *


class Test_StateModel(unittest.TestCase):
    """
    Test the state model class
    """

    def setUp(self):
        model = State()
        self.assertTrue(hasattr(model, "name"))
        self.assertEqual(model.name, "")


if __name__ == "__main__":
    unittest.main()
