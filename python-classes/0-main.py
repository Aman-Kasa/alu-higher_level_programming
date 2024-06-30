#!/usr/bin/python3
"""
0-main module

This module demonstrates the usage of the Square class defined in 0-square.py.

"""

if __name__ == "__main__":
    # Define the Square class inline (not importing directly)
    class Square:
        """
        Empty class Square

        Defines a square with no attributes or methods.

        """
        pass
    
    # Create an instance of Square
    my_square = Square()
    
    # Print the type and dictionary representation of my_square
    print(type(my_square))
    print(my_square.__dict__)
