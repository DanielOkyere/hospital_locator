from api.models import users
import unittest
from api.database import Base
from sqlalchemy import Column, Integer, String, Boolean

class TestUser(unittest.TestCase):
    """ Test cases for the user class """
    def test_user_attrs(self):
        """Test that all public attributes of user exists"""
        u = User()
        self.assertTrue('id' in self.u)
        self.assertTrue('email' in self.u)
        self.assertTrue('hashed_password' in self.u)
        self.assertTrue('is_active' in self.u)
        self.assertTrue('first_name' in self.u)
        self.assertTrue('last_name' in self.u)

    def test_user_attrs_type(self):
        """test the variable types the User class attributes accepts"""
        u = User()
        self.assertEqual(type(self.u.id), int)
        self.assertEqual(type(self.u.email), str)
        self.assertEqual(type(self.u.hashed_password), str)
        self.assertEqual(type(self.u.is_active), bool)
        self.assertEqual(type(self.u.first_name), str)
        self.assertEqual(type(self.u.last_name), str)
