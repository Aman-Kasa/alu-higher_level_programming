#!/usr/bin/python3
""" Rectangle class that inherits from Base """

from models.base import Base


class Rectangle(Base):
    """ Rectangle class that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize Rectangle instance """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Get the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width with validation """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Get the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height with validation """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Get the x coordinate """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set the x coordinate with validation """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Get the y coordinate """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set the y coordinate with validation """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculate the area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ Print the rectangle with # considering x and y """
        print("\n" * self.__y, end="")
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ Return the string representation of the rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args):
        """ Update attributes of the rectangle """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
