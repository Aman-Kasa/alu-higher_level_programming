#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_no_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id(self):
        b = Base(89)
        self.assertEqual(b.id, 89)


if __name__ == "__main__":
    unittest.main()
