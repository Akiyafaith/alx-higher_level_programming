#!/usr/bin/python3
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
"""define a class containing the test cases"""


class TestBase(unittest.TestCase):
    def test_id(self):
        b1 = Base()
        b2 = Base(98)
        b3 = Base()
        b4 = Base(1)
        b5 = Base(0)
        b6 = Base(-3)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 98)
        self.assertEqual(b3.id, 2)
        self.assertEqual(b4.id, 1)
        self.assertEqual(b5.id, 0)
        self.assertEqual(b6.id, -3)

    def test_json_string(self):
        """test for the json_string method"""
        b1 = Base()
        b2 = Base(98)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(type(Base.to_json_string([{}])), str)
        self.assertEqual(Base.to_json_string([{}]), "[{}]")
        self.assertEqual(
            type(Base.to_json_string([
                b1.to_dictionary(),
                b2.to_dictionary()
            ])),
            str)
        self.assertEqual(
            Base.to_json_string([b1.to_dictionary(), b2.to_dictionary()]),
            '[{"id": 1}, {"id": 98}]')

    def test_save_to_file(self):
        b1 = Base()
        b2 = Base(98)
        Base.save_to_file([b1, b2])
        with open("Base.json", "r") as fn:
            self.assertEqual(
                json.loads(file.read()), [
                    b1.to_dictionary(),
                    b2.to_dictionary()
                ])

    def test_load_from_file(self):
        b1 = Base()
        b2 = Base(98)
        Base.save_to_file([b1, b2])
        obj = Base.load_from_file()
        self.assertEqual(len(obj), 2)
        self.assertIsInstance(obj[0], Base)
        self.assertIsInstance(obj[1], Base)
        self.assertEqual(obj[0].id, 1)
        self.assertEqual(obj[1].id, 98)


if __name__ == "__main__":
    unittest.main()
