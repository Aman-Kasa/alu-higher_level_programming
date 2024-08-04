#!/usr/bin/python3
"""
Unit tests for the Rectangle class.
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unit tests for the Rectangle class."""

    def test_id_assignment(self):
        """Test id assignment."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_getters_setters(self):
        """Test getter and setter methods."""
        r = Rectangle(10, 2, 3, 4)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        r.width = 15
        r.height = 5
        r.x = 6
        r.y = 7
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 6)
        self.assertEqual(r.y, 7)


if __name__ == "__main__":
    unittest.main()
