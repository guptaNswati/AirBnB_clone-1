import unittest
from datetime import datetime
from models import *


class Test_AmenityModel(unittest.TestCase):
    """
    Test the amenity model class
    """

    def setUp(self):
        model = Amenity()
        self.assertTrue(hasattr(model, "name"))
        self.assertEqual(model.name, "")


if __name__ == "__main__":
    unittest.main()
