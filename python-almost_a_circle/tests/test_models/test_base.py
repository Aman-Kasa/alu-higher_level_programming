#!/usr/bin/python3
"""
Unit tests for the Base class.
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unit tests for the Base class."""

    def setUp(self):
        """Reset the Base class object count before each test."""
        Base._Base__nb_objects = 0

    def test_default_id(self):
        """Test default id assignment."""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_custom_id(self):
        """Test custom id assignment."""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
        b2 = Base()
        self.assertEqual(b2.id, 1)

    def test_mixed_id(self):
        """Test mixed default and custom id assignment."""
        b1 = Base()
        b2 = Base(5)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 5)
        self.assertEqual(b3.id, 2)


if __name__ == "__main__":
    unittest.main()
