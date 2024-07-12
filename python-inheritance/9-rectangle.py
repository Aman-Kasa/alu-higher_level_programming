#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry"""

    def __init__(self, width=None, height=None):
        """Initialize a new Rectangle instance"""
        if width is not None:
            self.integer_validator("width", width)
            self.__width = width
        else:
            self.__width = 0
        if height is not None:
            self.integer_validator("height", height)
            self.__height = height
        else:
            self.__height = 0

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
