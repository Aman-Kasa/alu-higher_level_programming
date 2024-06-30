#!/usr/bin/python3
"""
3-main module

This module tests the Square class defined in 3-square.py.

"""

if __name__ == "__main__":
    Square = __import__('3-square').Square

    # Create Square with size 3
    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)  # Attempt to access size attribute
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)  # Attempt to access __size attribute
    except Exception as e:
        print(e)

    # Create Square with size 5
    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))
