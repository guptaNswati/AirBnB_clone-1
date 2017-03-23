import unittest
from datetime import datetime
from models import *


class Test_PlaceModel(unittest.TestCase):
    """
    Test the place model class
    """

    def setUp(self):
        self.model = Place()
        self.assertTrue(hasattr(model, "city_id"))
        self.assertTrue(hasattr(model, "user_id"))
        self.assertTrue(hasattr(model, "name"))
        self.assertTrue(hasattr(model, "description"))
        self.assertTrue(hasattr(model, "number_rooms"))
        self.assertTrue(hasattr(model, "number_bathrooms"))
        self.assertTrue(hasattr(model, "max_guest"))
        self.assertTrue(hasattr(model, "price_by_night"))
        self.assertTrue(hasattr(model, "latitude"))
        self.assertTrue(hasattr(model, "longitude"))
        self.assertTrue(hasattr(model, "amenities"))
        self.assertEqual(model.city_id, "")
        self.assertEqual(model.user_id, "")
        self.assertEqual(model.name, "")
        self.assertEqual(model.description, "")
        self.assertEqual(model.number_rooms, 0)
        self.assertEqual(model.number_bathrooms, 0)
        self.assertEqual(model.max_guest, 0)
        self.assertEqual(model.price_by_night, 0)
        self.assertEqual(model.latitude, 0.0)
        self.assertEqual(model.longitude, 0.0)
        self.assertEqual(model.amenities, [''])


if __name__ == "__main__":
    unittest.main()
