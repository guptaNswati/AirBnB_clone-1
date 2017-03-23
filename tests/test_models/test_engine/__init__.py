#!/usr/bin/python3
import os
from models import *

if os.getenv('HBNB_TYPE_STORAGE') != 'db':
    from tests.test_models.test_engine.test_file_storage import Test_FileStorage
    test_storage = test_file_storage.Test_FileStorage()
else:
    from tests.test_models.test_engine.test_db_storage import Test_DBStorage
    test_storage = test_db_storage.Test_DBStorage()
test_storage.reload()
