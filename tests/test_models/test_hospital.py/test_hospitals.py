from api.database import Base
from sqlalchemy import Column, Integer, String, Boolean
import unittest
from api.model.hospital import Hospital

class TestHospital(unittest.TestCase):
    """Test cases for the hospital class"""
    def_test_hospital_attrs(self):
        #test that atrributes of the hospital class exists
        h = Hospital()
        self.assertTrue('id' in self.h)
        self.assertTrue('name' in self.h)
        self.assertTrue('coordinates' in self.h)
        self.assertTrue('longitude' in self.h)
        self.assertTrue('latitide' in self.h)
        self.assertTrue('specialisation' in self.h)
        self.assertTrue('address' in self.h)

    def_test_hospital_attrs_type(self):
        #test the variable types the hospital class atrributes accepts
        h = Hospital()
        self.assertEqual(type(self.h.id), int)
        self.assertEqual(type(self.h.name), string)
        self.assertEqual(type(self.h.longitudes), float)
        self.assertEqual(type(self.h.latitude), float)
        self.assertEqual(type(self.h.specialisatuon), string)
        self.assertEqual(type(self.h.address), string)

    def test_issubclass(self):
        #test that the Hospital class is a subclass of Base
        h = Hospital()
        self.assertTrue(issubclass(type(self.h), Base)

if __name__ == "__main__":
        unittest.main()
