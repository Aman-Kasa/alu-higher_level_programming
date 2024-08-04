#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base"""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width attribute with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height attribute with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x attribute with validation"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y attribute with validation"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @staticmethod
    def to_csv_list(obj):
        """Convert a Rectangle object to a CSV list"""
        return [obj.id, obj.width, obj.height, obj.x, obj.y]
