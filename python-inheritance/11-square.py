#!/usr/bin/python3
"""
This module defines the `Square` class, inheriting from `Rectangle`.
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A class called Square that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize the Square with a size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size  # private attribute

    def __str__(self):
        """Return a string representation of the Square."""
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """Return the area of the Square."""
        return self.__size ** 2
