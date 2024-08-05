#!/usr/bin/python3
"""
Unit tests for models/rectangle.py
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def test_id_provided(self):
        """
        Test initialization with provided id.
        """
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_id_not_provided(self):
        """
        Test initialization without provided id.
        """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_getters_and_setters(self):
        """
        Test getters and setters.
        """
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        r.width = 15
        r.height = 5
        r.x = 1
        r.y = 1
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)


if __name__ == '__main__':
    unittest.main()
