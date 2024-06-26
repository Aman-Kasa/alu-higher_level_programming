#!/usr/bin/python3


def uniq_add(my_list=[]):
    unique_sum = 0
    seen_numbers = set()
    for num in my_list:
        if num not in seen_numbers:
            unique_sum += num
            seen_numbers.add(num)
    return unique_sum


if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
