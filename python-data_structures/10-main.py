#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

test_cases = [
    [1, 2, 3, 4],
    [0, 1, 2, 3],
    [0, 1],
    []
]

for my_list in test_cases:
    list_result = divisible_by_2(my_list)
    for i in range(len(list_result)):
        print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    print()  # For better readability of output
