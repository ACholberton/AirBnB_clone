#!/usr/bin/python3
""" Test for User class"""

import unittest
from datetime import date, time, datetime
import uuid
from models import storage
from models.user import User
import os
import time
import pep8


class Test_User(unittest.TestCase):
    """ Test For user class"""

    def setUp(self):
        """ Move Json files if they exist """
        if os.path.isfile("file.json"):
            os.rename("file.json", "file.json.temp")

    def tearDown(self):
        """ Delete test files and put original files back"""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        if os.path.isfile("file.json.temp"):
            os.rename("file.json.temp", "file.json")

    def test_pep8(self):
        """ checks for pep8 compliance """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(["models/user.py"])
        self.assertEqual(result.total_errors, 0,
                         "found code style errors and warnings")

    def test_defaultAttribute(self):
        """ check for id, created_at, updated_at default attributes """
        b = User()
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))
        self.assertTrue(hasattr(b, "email"))
        self.assertTrue(hasattr(b, "password"))
        self.assertTrue(hasattr(b, "first_name"))
        self.assertTrue(hasattr(b, "last_name"))
        self.assertEqual(type(b.updated_at), datetime)
        self.assertEqual(type(b.created_at), datetime)
        self.assertEqual(type(b.id), str)
        self.assertFalse(hasattr(b, "Potato"))
        self.assertEqual(type(b.email), str)
        self.assertEqual(type(b.password), str)
        self.assertEqual(type(b.first_name), str)
        self.assertEqual(type(b.last_name), str)

    def test_assignAtt(self):
        """ Test assigned attributes"""
        c = User()
        c.text1 = "Pizza"
        c.text2 = "sashimi"
        self.assertEqual(type(c.text1), str)
        self.assertEqual(type(c.text2), str)

    def test_save(self):
        """ checks if updated_at is saved """
        d = User()
        e = d.updated_at
        time.sleep(0.1)
        d.save()
        f = d.updated_at
        self.assertNotEqual(f, e)

    def test_to_dict(self):
        """ dictionary conversion test """
        i = User()
        i.name = "Cute_anime_girl"
        i.number = 25
        j = i.to_dict()
        self.assertTrue("name" in j)
        self.assertEqual(type(j["name"]), str)
        self.assertTrue("number" in j)
        self.assertEqual(type(j["number"]), int)
        self.assertTrue("created_at" in j)
        self.assertTrue("updated_at" in j)
        self.assertTrue("id" in j)

    def test_reCreate_kwarg(self):
        """Recreate dictionary from saved dictionary"""
        k = User()
        k.name = "Cute_anime_girl"
        k.number = 99
        j = k.to_dict()
        l = User(**j)
        self.assertEqual(k.name, l.name)
        self.assertEqual(k.number, l.number)
        self.assertEqual(k.id, l.id)
        self.assertEqual(k.created_at, l.created_at)
        self.assertEqual(k.updated_at, l.updated_at)
        self.assertEqual(type(k.id), str)
        self.assertFalse(k is j)

    def test_timeFormat(self):
        """ check Created_at and Updated_at values"""
        l = User()
        m = "%Y-%m-%dT%H:%M:%S.%f"
        n = l.to_dict()
        self.assertEqual(n["created_at"], l.created_at.strftime(m))
        self.assertEqual(n["updated_at"], l.updated_at.strftime(m))


if __name__ == '__main__':
    unittest.main()
