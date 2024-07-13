#!/usr/bin/python3
MyInt = __import__('100-my_int').MyInt

my_i = MyInt(3)
print(my_i)       # Should print: 3
print(my_i == 3)  # Should print: False (inverted equality)
print(my_i != 3)  # Should print: True (inverted inequality)
