"""Test suite for the api.models.schemas.py module"""
from api.database import Base
from api.models import schemas.py
import unittest

class TestUser(unittest.TestCase):
    #testing the schema module
    def setUpClass(self):
        #Set up class instance for tests
        self.user_base = UserBase()
        self.user_create = UserCreate()
        self.user = User()

    def test_issubclass(self):
        """Test that UserBase is a sub-class of BaseModel,
        UserCreate and User are subclasses of UserBase"""
        self.assertTrue(issubclass(type(self.user_base), BaseModel))
        self.assertTrue(issubclass(type(self.user_create), UserBase))
        self.assertTrue(issubclass(type(self.user), UserBase))

    def test_user_base_attrs(self):
        #test that the attribute of the UserBase class exists
        self.assertTrue(hasattr(UserBase, "email"))

    def test_user_create_attrs(self):
        #test that all attributes of UserCreate class exists
        self.assertTrue('password' in self.user_create)
        self.assertTrue('first_name' in self.user_create)
        self.assertTrue('last_name' in self.user_create)

    def test_user_attrs(self):
        #test that the attributes of the User class exists
        self.assertTrue('id' in self.user)
        self.assertTrue('is_active' in self.user)

    def test_attributes_type_is_string(self):
        """testing the variable types the class attributes accept"""
        self.assertEqual(type(self.user_base.email), str)
        self.assertEqual(type(self.user_create.password), str)
        self.assertEqual(type(self.user_create.first_name), str)
        self.assertEqual(type(self.user_create.last_name), str)
        self.assertEqual(type(self.user.id), int)
        self.assertEqual(type(self.user.is_active), bool)

if __name__ == "__main__":
        unittest.main()
