#!/usr/bin/python3
"""
Unit tests for models/base.py
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def test_id_provided(self):
        """
        Test initialization with provided id.
        """
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_id_not_provided(self):
        """
        Test initialization without provided id.
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_mixed(self):
        """
        Test mixed initialization with and without provided id.
        """
        b1 = Base()
        b2 = Base(5)
        b3 = Base()
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 5)
        self.assertEqual(b3.id, 2)
        self.assertEqual(b4.id, 3)


if __name__ == '__main__':
    unittest.main()
