#!/usr/bin/python3
number = 98

try:
    print(f"{number} Battery street")
except TypeError:
    print("ValueError: Unknown format code 'd' for object of type 'str'")
