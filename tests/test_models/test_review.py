import unittest
from datetime import datetime
from models import *


class Test_ReviewModel(unittest.TestCase):
    """
    Test the review model class
    """

    def setUp(self):
        model = Review()
        self.assertTrue(hasattr(model, "place_id"))
        self.assertTrue(hasattr(model, "user_id"))
        self.assertTrue(hasattr(model, "text"))
        self.assertEqual(model.place_id, "")
        self.assertEqual(model.user_id, "")
        self.assertEqual(model.text, "")


if __name__ == "__main__":
    unittest.main()
