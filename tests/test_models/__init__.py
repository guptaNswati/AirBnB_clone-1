#!/usr/bin/python3
import os
from models import *
from tests import *


if os.getenv('HBNB_TYPE_STORAGE') != 'db':
    from tests.test_models.test_engine.test_file_storage import Test_FileStorage
    test_storage = Test_FileStorage()
else:
    from tests.test_models.test_engine.test_db_storage import Test_DBStorage
    test_storage = Test_DBStorage()
