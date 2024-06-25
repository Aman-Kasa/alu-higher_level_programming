#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list[:]  # Return a copy of the original list

    # Create a copy of the original list
    new_list = my_list[:]
    # Replace the element at index idx with new_element
    new_list[idx] = element
    return new_list


# Test cases as per the provided examples
if __name__ == "__main__":
    cases = [
        ([1, 2, 3], 1, 4),
        ([1, 2, 3], 0, 4),
        ([1, 2, 3], 2, 4),
        ([1, 2, 3], 3, 4),
        ([1, 2, 3], -1, 4),
        ([1], 0, 4),
        ([0], 0, 4)
    ]

    for my_list, idx, element in cases:
        new_list = new_in_list(my_list, idx, element)
        print(f"Correct output - case: list = {my_list} / "
              f"idx = {idx} / element = {element}")
        print(new_list)
