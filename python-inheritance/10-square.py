#!/usr/bin/python3

"""
Module documentation for Square class.
"""


class Rectangle:
    """
    Rectangle class for representing a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle with width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Computes the area of the rectangle.
        """
        return self.width * self.height


class Square(Rectangle):
    """
    Square class inherits from Rectangle, representing a square.
    """

    def __init__(self, size):
        """
        Initializes a square with a given size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return f"[Square] {self.width}/{self.height}"

    def integer_validator(self, name, value):
        """
        Validates that the value is a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def area(self):
        """
        Computes the area of the square.
        """
        return self.width * self.height


# Test cases
if __name__ == "__main__":
    # Test case 1: Print dir(Square)
    print(dir(Square))

    # Test case 2: Print issubclass(Square, Rectangle)
    print(issubclass(Square, Rectangle))

    # Test case 3: Create a Square instance with size 4
    s = Square(4)

    # Test case 4: Print area of square with size 4
    print(s.area())

    # Test case 5: Create a Square instance with size 1340
    s = Square(1340)
    print(s.area())

    # Test case 6: Create a Square instance with default size (error expected)
    try:
        s = Square()
    except TypeError as e:
        print(e)

    # Test case 7: Create a Square instance with size "13" (error expected)
    try:
        s = Square("13")
    except TypeError as e:
        print(e)

    # Test case 8: Create a Square instance with size 13
    s = Square(13)
    print(s.width)
    print(s.height)
