#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    printed_count = 0
    while count < x:
        try:
            print("{:d}".format(my_list[count]), end="")
            printed_count += 1
        except (ValueError, TypeError):
            pass
        except IndexError:
            import sys
            print("\nTraceback (most recent call last):", file=sys.stderr)
            break
        count += 1
    print()
    return printed_count
