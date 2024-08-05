#!/usr/bin/python3
"""Module defining a Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Class representing a rectangle, inheriting from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("width must be a positive integer")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("height must be a positive integer")
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinate of the rectangle"""
        if not isinstance(value, int) or value < 0:
            raise ValueError("x must be a non-negative integer")
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate of the rectangle"""
        if not isinstance(value, int) or value < 0:
            raise ValueError("y must be a non-negative integer")
        self.__y = value
