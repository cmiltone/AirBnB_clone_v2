#!/usr/bin/python3
"""test user"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import os


class test_User(test_basemodel):
    """test user class"""

    def __init__(self, *args, **kwargs):
        """init"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """first name tst"""
        new = self.value()
        self.assertEqual(type(new.first_name), str if
                os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                type(None))

    def test_last_name(self):
        """last name test"""
        new = self.value()
        self.assertEqual(type(new.last_name), str if
                os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                type(None))

    def test_email(self):
        """email test"""
        new = self.value()
        self.assertEqual(type(new.email), str if
                os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                type(None))

    def test_password(self):
        """passwrd user test"""
        new = self.value()
        self.assertEqual(type(new.password), str if
                os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                type(None))
