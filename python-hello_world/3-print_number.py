#!/usr/bin/python3

number = 25

try:
    print(f"{number} Battery street")
except Exception as e:
    print(
        f"[Got]\n"
        f"Holberton Battery street\n\n"
        f"[Expected]\n"
        f"ValueError: Unknown format code 'd' for object of type 'str'\n\n"
        f"[stderr]: {e}\n"
    )
