#!/usr/bin/python3
"""
4-square module

This module defprivate size attribute, size validation, area method,
and getter/setter methods for size.

"""


class Square:
    """
    Square class

    Defines a sulation, and getter/setter for size.

    """

    def __init__(self, size=0):
        """
        Initializes a square with a specific size.

        Args:
            size (int, optional): Size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        self.size = size  # Calls setter method for validation

    @property
    def size(self):
        """
        Getter method for size attribute.

        Returns:
            int: Size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size attribute.

        Args:
            value (int): New size value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: Area of the square (size * size).

        """
        return self.__size ** 2


if __name__ == "__main__":
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
