#!/usr/bin/python3
"""
1-main module

This module tests the Square class defined in 1-square.py.

"""

if __name__ == "__main__":
    Square = __import__('1-square').Square

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
