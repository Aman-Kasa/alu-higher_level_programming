#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))        # Expected output: 3
print(add_integer(100, -2))     # Expected output: 98
print(add_integer(2))           # Expected output: 100
print(add_integer(100.3, -2))   # Expected output: 98
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)                   # Expected output: b must be an integer
try:
    print(add_integer(None))
except Exception as e:
    print(e)                   # Expected output: a must be an integer
