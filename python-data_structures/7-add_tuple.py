#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    # Handle tuple_a
    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0,) * (2 - len(tuple_a))
    else:
        tuple_a = tuple_a[:2]  # Take only the first two elements

    # Handle tuple_b
    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0,) * (2 - len(tuple_b))
    else:
        tuple_b = tuple_b[:2]  # Take only the first two elements

    # Perform addition
    result_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return result_tuple


if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)  # Output: (89, 100)

    print(add_tuple(tuple_a, (1, )))  # Output: (2, 89)
    print(add_tuple(tuple_a, ()))     # Output: (1, 89)
