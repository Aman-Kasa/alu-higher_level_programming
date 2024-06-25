#!/usr/bin/python3


def max_integer(my_list=[]):
    if not my_list:
        return None  # Return None for empty list

    max_value = my_list[0]  # Initialize max_value with the first element

    for num in my_list[1:]:
        if num > max_value:
            max_value = num  # Update max_value if we find a larger number

    return max_value


if __name__ == "__main__":
    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))
