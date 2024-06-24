def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)  # c = 25 when a = 10, b = 15
        for i in range(4, 6):
            c = add(c, i)  # c = 29 after i = 4, c = 34 after i = 5
        return c  # should return 34 for a = 10, b = 15
    else:
        return sub(a, b)
