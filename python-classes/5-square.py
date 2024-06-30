#!/usr/bin/python3
"""
5-square module

This module def Square class with a private size attribute, size validation,
area method, and a method to print the square pattern.

"""


class Square:
    """
    Square class

    Defines a swith validation, area calculation, and printing functionality.

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

    def my_print(self):
        """
        Prints a square pattern of '#' characters to represent the square.

        If size is 0, prints an empty line.

        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)


if __name__ == "__main__":
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
