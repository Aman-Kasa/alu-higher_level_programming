#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

print(my_rectangle_1 == Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2))
print(my_rectangle_2 == Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2))

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(4, 8)

print(my_rectangle_1 == Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2))
print(my_rectangle_2 == Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2))

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(1, 8)

try:
    print(my_rectangle_2 == Rectangle.bigger_or_equal(my_rectangle_1, "Rect"))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    print(my_rectangle_2 == Rectangle.bigger_or_equal("Rect", my_rectangle_1))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
