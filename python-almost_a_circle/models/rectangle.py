#!/usr/bin/python3
"""
Module for defining the Rectangle class.

This module contains the definition of the Rectangle class, which is a
subclass of Base. It represents a rectangle with width, height, and
coordinates (x, y), and it provides methods to access and modify these
attributes.
"""

from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle with width, height, and coordinates.

    Inherits from Base.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x coordinate of the rectangle.
        y (int): The y coordinate of the rectangle.
        id (int): The id of the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None): a new Rectangle instance.
        width(self): Gets the width of the rectangle.
        width(self, value): Sets the width of the rectangle.
        height(self): Gets the height of the rectangle.
        height(self, value): Sets the height of the rectangle.
        x(self): Gets the x coordinate of the rectangle.
        x(self, value): Sets the x coordinate of the rectangle.
        y(self): Gets the y coordinate of the rectangle.
        y(self, value): Sets the y coordinate of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x coordinate of the ctangle. Defaultsto0.
            y (int, optional): The y coordinate of the rectangle. Defaultsto0.
            id (int, optional): The id of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinate of the rectangle."""
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate of the rectangle."""
        self.__y = value
