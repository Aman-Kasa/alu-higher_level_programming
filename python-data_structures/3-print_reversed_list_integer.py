#!/usr/bin/python3


def print_reversed_list_integer(my_list=None):
    if my_list is None:
        return
    if not isinstance(my_list, list):
        return
    for i in range(len(my_list) - 1, -1, -1):
        if isinstance(my_list[i], int):
            print("{:d}".format(my_list[i]))
        else:
            raise TypeError("List contains non-integer values")


# Test case as per the provided example
if __name__ == "__main__":
    list1 = [1, 2, 3]
    list2 = [1]
    list3 = []
    list4 = None
    list5 = [1, 2, "H", 9]

    print("Correct output - case: list =", list1)
    print_reversed_list_integer(list1)

    print("\nCorrect output - case: list =", list2)
    print_reversed_list_integer(list2)

    print("\nCorrect output - case: list =", list3)
    print_reversed_list_integer(list3)

    print("\nCorrect output - case: list =", list4)
    print_reversed_list_integer(list4)

    print("\nCorrect output - case: list =", list5)
    try:
        print_reversed_list_integer(list5)
    except TypeError as e:
        print(e)
