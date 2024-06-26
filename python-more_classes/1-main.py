#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)  # Output: {'_Rectangle__height': 4, '_Rectangle__width': 2}

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)  # Output: {'_Rectangle__height': 3, '_Rectangle__width': 10}
