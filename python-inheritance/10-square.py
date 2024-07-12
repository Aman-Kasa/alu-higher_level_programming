#!/usr/bin/python3
"""
This module defines the `Square` class, inheriting from `Rectangle`.
"""


class Rectangle:
    """A class Rectangle with width and height attributes."""
    def __init__(self, width, height):
        """Initialize the Rectangle with width and height."""
        self.width = width
        self.height = height

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return f"[Rectangle] {self.width}/{self.height}"

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def integer_validator(self, name, value):
        """Validate integer values."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")


class Square(Rectangle):
    """A class Square that inherits from Rectangle."""
    def __init__(self, size):
        """Initialize the Square with a size."""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the Square."""
        return f"[Square] {self.__size}/{self.__size}"

    @property
    def size(self):
        """Getter for size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size attribute."""
        self.__size = value
        self.integer_validator("size", value)
        self.width = value
        self.height = value
