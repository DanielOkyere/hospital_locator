"""Test suite for the api.models.schemas.py module"""
from api.database import Base
from api.models.user import schemas
from api.models.user.users import User
import unittest

class TestUser(unittest.TestCase):
    #testing the schema module
    def setUpClass(self):
        #Set up class instance for tests
        self.user_base = schemas.UserBase()
        self.user_create = schemas.UserCreate()
        self.user_schema = schemas.UserSchema()
        self.user_token = schemas.Token()

    def test_issubclass(self):
        """Test that UserBase, Token are sub-classes of BaseModel,
        UserCreate, UserSchema and User are subclasses of UserBase"""
        self.assertTrue(issubclass(type(self.user_base), BaseModel))
        self.assertTrue(issubclass(type(self.user_create), UserBase))
        self.assertTrue(issubclass(type(self.user_schema), UserBase))
        self.assertTrue(issubclass(type(self.user_token), Base model))

    def test_user_base_attrs(self):
        #test that the attribute of the UserBase class exists
        self.assertTrue(hasattr(UserBase, "email"))

    def test_user_create_attrs(self):
        #test that all attributes of UserCreate class exists
        self.assertTrue('password' in self.user_create)
        self.assertTrue('first_name' in self.user_create)
        self.assertTrue('last_name' in self.user_create)
       
    def test_attributes_type_is_string(self):
        """testing the variable types the class attributes accept"""
        self.assertEqual(type(self.user_base.email), str)
        self.assertEqual(type(self.user_create.password), str)
        self.assertEqual(type(self.user_create.first_name), str)
        self.assertEqual(type(self.user_create.last_name), str)
        self.assertEqual(type(self.user.id), int)
        self.assertEqual(type(self.user.is_active), bool)

    def test_user_schema_attrs(self):
        #test that the attributes of the UserSchema class exists
        self.assertTrue('id' in self.user_schema)
        self.assertTrue('is_active' in self.user_schema)
        self.assertTrue('first_name' in self.user_schema)
        self.assertTrue('last_name' in self.user_schema)

if __name__ == "__main__":
        unittest.main()
