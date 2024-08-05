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

    def test_invalid_width(self):
        """
        Test setting invalid width.
        """
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

    def test_invalid_height(self):
        """
        Test setting invalid height.
        """
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            Rectangle(10, -2)

    def test_invalid_x(self):
        """
        Test setting invalid x.
        """
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "0")
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1)

    def test_invalid_y(self):
        """
        Test setting invalid y.
        """
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, "0")
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -1)

    def test_area(self):
        """
        Test the area method.
        """
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """
        Test the display method.
        """
        r1 = Rectangle(4, 6)
        r2 = Rectangle(2, 2)
        
        expected_output_1 = "####\n####\n####\n####\n####\n####\n"
        expected_output_2 = "##\n##\n"

        f = StringIO()
        with redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), expected_output_1)

        f = StringIO()
        with redirect_stdout(f):
            r2.display()
        self.assertEqual(f.getvalue(), expected_output_2)

    def test_str(self):
        """
        Test the __str__ method.
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)

        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")


if __name__ == '__main__':
    unittest.main()
