"""Test suite for the api.models.schemas.py module"""
from api.database import Base
from api.models import schemas.py
import unittest

class TestUserBase(unittest.TestCase):
    #test for the UserBase class
    def setUpClass(self):
        #Set up class instance for tests
        self.user_base = UserBase()

    def test_issubclass(self):
        """Test that UserBase is a sub-class of BaseModel"""
        self.assertTrue(issubclass(type(self.user_base), BaseModel))
