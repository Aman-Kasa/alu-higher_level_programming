#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            element = my_list[i]
            try:
                print("{:d}".format(element), end="")
                count += 1
            except (ValueError, TypeError):
                continue
        except IndexError:
            break
    print()  # For a new line after the loop
    return count
