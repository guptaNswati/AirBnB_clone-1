import unittest
from datetime import datetime
from models import *


class Test_CityModel(unittest.TestCase):
    """
    Test the city model class
    """

    def setUp(self):
        model = City()
        self.assertTrue(hasattr(model, "name"))
        self.assertTrue(hasattr(model, "state_id"))
        self.assertEqual(model.name, "")
        self.assertEqual(model.state_id, "")


if __name__ == "__main__":
    unittest.main()
