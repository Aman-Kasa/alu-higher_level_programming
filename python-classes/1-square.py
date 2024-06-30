#!/usr/bin/python3
"""
1-square module

This module defines a Square class with a private size attribute.

"""


class Square:
    """
    Square class

    Defines a square by its size.

    """

    def __init__(self, size):
        """
        Initializes a square with a specific size.

        Args:
            size (int): Size of the square.

        """
        self.__size = size

if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
