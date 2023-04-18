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
        self.token = schemas.Token()
        self.token_data = schemas.TokenData()

    def test_issubclass(self):
        """Test that UserBase, Token, TokenData are sub-classes of BaseModel,
        UserCreate, UserSchema and User are subclasses of UserBase"""
        self.assertTrue(issubclass(type(self.user_base), BaseModel))
        self.assertTrue(issubclass(type(self.user_create), UserBase))
        self.assertTrue(issubclass(type(self.user_schema), UserBase))
        self.assertTrue(issubclass(type(self.token), BaseModel))
        self.assertTrue(issubclass(type(self.token_data), BaseModel))

    def test_user_base_attrs(self):
        #test that the attribute of the UserBase class exists
        self.assertTrue(hasattr(UserBase, "email"))

    def test_user_create_attrs(self):
        #test that all attributes of UserCreate class exists
        self.assertTrue('password' in self.user_create)
        self.assertTrue('first_name' in self.user_create)
        self.assertTrue('last_name' in self.user_create)
       
    def test_attributes_type(self):
        """testing the variable types the class attributes accept"""
        self.assertEqual(type(self.user_base.email), str)
        self.assertEqual(type(self.user_create.password), str)
        self.assertEqual(type(self.user_create.first_name), str)
        self.assertEqual(type(self.user_create.last_name), str)
        self.assertEqual(type(self.user_schema.id), int)
        self.assertEqual(type(self.user_schema.is_active), bool)
        self.assertEqual(type(self.user_schema.first_name), str)
        self.assertEqual(type(self.user_schema.last_name), str)
        self.assertEqual(type(self.token.access_token), str)
        self.assertEqual(type(self.token.token_type), str)
        self.assertEqual(type(self.token_data.email), str)

    def test_user_schema_attrs(self):
        #test that the attributes of the UserSchema class exists
        self.assertTrue('id' in self.user_schema)
        self.assertTrue('is_active' in self.user_schema)
        self.assertTrue('first_name' in self.user_schema)
        self.assertTrue('last_name' in self.user_schema)

    def test_user_token_attrs(self):
        #test that the attributes of the Token class exists
        self.assertTrue('access_token' in self.token)
        self.assertTrue('token_type' in self.token)
    
    def test_token_data_attrs(self):
        #test that the attributes of TokenData class exists
        self.assertTrue(hasattr(TokenData, "email"))

if __name__ == "__main__":
        unittest.main()
