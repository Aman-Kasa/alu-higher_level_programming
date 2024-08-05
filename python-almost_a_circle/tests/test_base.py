#!/usr/bin/python3
"""Unit tests for Base class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os

class TestBase(unittest.TestCase):
    """Tests for Base class."""

    def setUp(self):
        """Reset the number of objects before each test."""
        Base._Base__nb_objects = 0

    def test_save_to_file_csv(self):
        """Test saving list of instances to CSV file."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles)

        with open("Rectangle.csv", "r") as file:
            content = file.readlines()
        self.assertEqual(content[0].strip(), "1,10,7,2,8")
        self.assertEqual(content[1].strip(), "2,2,4,0,0")

    def test_load_from_file_csv(self):
        """Test loading list of instances from CSV file."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles)
        loaded_rectangles = Rectangle.load_from_file_csv()

        self.assertEqual(len(loaded_rectangles), 2)
        self.assertEqual(str(loaded_rectangles[0]), str(r1))
        self.assertEqual(str(loaded_rectangles[1]), str(r2))

    def test_save_to_file_csv_square(self):
        """Test saving list of Square instances to CSV file."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares = [s1, s2]
        Square.save_to_file_csv(list_squares)

        with open("Square.csv", "r") as file:
            content = file.readlines()
        self.assertEqual(content[0].strip(), "1,5,0,0")
        self.assertEqual(content[1].strip(), "2,7,9,1")

    def test_load_from_file_csv_square(self):
        """Test loading list of Square instances from CSV file."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares = [s1, s2]
        Square.save_to_file_csv(list_squares)
        loaded_squares = Square.load_from_file_csv()

        self.assertEqual(len(loaded_squares), 2)
        self.assertEqual(str(loaded_squares[0]), str(s1))
        self.assertEqual(str(loaded_squares[1]), str(s2))

    def tearDown(self):
        """Clean up any created files after each test."""
        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")
        if os.path.exists("Square.csv"):
            os.remove("Square.csv")

if __name__ == "__main__":
    unittest.main()
