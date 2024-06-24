#!/usr/bin/python3

def magic_calculation(a, b):
    add, sub = None, None  # Placeholder for add and sub functions

    # Check if a < b
    if a < b:
        c = add(a, b)
    else:
        c = sub(a, b)

    # Loop 4 times and call add(c, i) inside the loop
    for i in range(4, 6):
        c = add(c, i)

    return c
