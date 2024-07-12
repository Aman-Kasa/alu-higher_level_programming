#!/usr/bin/python3
BaseGeometry = __import__('5-base_geometry').BaseGeometry

bg = BaseGeometry()

print(bg)           # Print the object representation
print(dir(bg))      # Print the attributes and methods of bg
print(dir(BaseGeometry))
