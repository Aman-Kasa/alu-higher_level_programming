def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # Try to access the element at index i
            element = my_list[i]
            try:
                # Try to print the element as an integer
                print("{:d}".format(element), end="")
                count += 1
            except (ValueError, TypeError):
                # Skip elements that are not integers
                continue
        except IndexError:
            # Break the loop if the index is out of range
            break
    print()  # For a new line after the loop
    return count
