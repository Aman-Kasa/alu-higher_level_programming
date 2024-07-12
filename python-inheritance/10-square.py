#!/usr/bin/python3
"""
Module for Square class.
"""
from typing import Union

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle.
    """

    def __init__(self, size: Union[int, float]):
        """
        Initializes the Square instance.

        Args:
            size (int): size of the square, must be a positive integer.
        """
        self.__size = 0
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self) -> int:
        """
        Computes the area of the square.

        Returns:
            int: Area of the square.
        """
        return self.__size * self.__size

    @property
    def size(self) -> int:
        """
        Getter for size attribute.

        Returns:
            int: size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value: Union[int, float]):
        """
        Setter for size attribute.

        Args:
            value (int): size of the square, must be a positive integer.
        """
        self.integer_validator("size", value)
        self.__size = value

    def integer_validator(self, name: str, value: Union[int, float]):
        """
        Validates the value as a positive integer.

        Args:
            name (str): name of the value being validated.
            value (int): value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def __str__(self) -> str:
        """
        Returns a string representation of the Square.

        Returns:
            str: [Square] <width>/<height>
        """
        return f"[Square] {self.__size}/{self.__size}"
