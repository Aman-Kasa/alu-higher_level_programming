#!/usr/bin/python3
""" 6-main """
from models.rectangle import Rectangle


if __name__ == "__main__":

    # Create a Rectangle with width 2, height 3, x offset 2, and y offset 2
    r1 = Rectangle(2, 3, 2, 2)
    r1.display()
    
    # Print a separator
    print("---")

    # Create a Rectangle with width 3, height 2, x offset 1, and y offset 0
    r2 = Rectangle(3, 2, 1, 0)
    r2.display()
