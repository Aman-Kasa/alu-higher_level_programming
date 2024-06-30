#!/usr/bin/python3
"""
6-square module

This module defines a Square class with private size and position attributes, size and position validation,
area method, and a method to print the square pattern.

"""


class Square:
    """
    Square class

    Defines a square by its size, position with validation, aren

    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with a specific size and position.

        Args:
            size (int, optional): Size of the square. Defaults to 0.
            position (tuple, optional): Position of the square.

        Raises:
            TypeError: If size is a tuple of two positive integers.
            ValueError: If size iontains non-positive integers.

        """
        self.size = size  # Calls setter method for size validation
        self.position = position  # Calls setter method for position

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

    @property
    def position(self):
        """
        Getter method for position attribute.

        Returns:
            tuple: Position of the square.

        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for position attribute.

        Args:
            value (tuple): New position value to set.

        Raises:
            TypeError: If value is not a tuple of two positive integers.
            ValueError: If value contains non-positive integers.

        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(i, int) and i >= 0 for i in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
        Uses position to determine starting row and column.

        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)


if __name__ == "__main__":
    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")
