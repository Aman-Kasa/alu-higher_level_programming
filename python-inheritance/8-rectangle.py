#!/usr/bin/python3
"""
Module for Rectangle class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class, inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle instance.

        Args:
            width (int): width of the rectangle, must be a positive integer.
            height (int): height of the rectangle, must be a positive integer.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the Rectangle.

        Returns:
            str: [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
