#!/usr/bin/python3
"""
Unit tests for my_module.py
"""

import unittest
from my_module import MyClass, my_function


class TestMyClass(unittest.TestCase):
    """
    Test cases for MyClass.
    """

    def test_my_method(self):
        """
        Test my_method of MyClass.
        """
        obj = MyClass()
        self.assertIsNone(obj.my_method())


class TestMyFunction(unittest.TestCase):
    """
    Test cases for my_function.
    """

    def test_my_function(self):
        """
        Test my_function.
        """
        self.assertIsNone(my_function())


if __name__ == '__main__':
    unittest.main()
