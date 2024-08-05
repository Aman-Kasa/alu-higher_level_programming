#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_initialization(self):
        r = Rectangle(10, 20, 5, 15)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 15)

    def test_invalid_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-10, 20)

    def test_invalid_height(self):
        with self.assertRaises(ValueError):
            Rectangle(10, -20)


if __name__ == "__main__":
    unittest.main()
