#!/usr/bin/python3
safe_print_list_integers = __import__('2-safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, 7)  # We can't use len(my_list)
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, 9)  # We can't use len(my_list) + 2
print("nb_print: {:d}".format(nb_print))

# Additional test cases
my_list = [1, 2, 3, 4]

nb_print = safe_print_list_integers(my_list, 4)  # Equivalent to len(my_list)
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, 2)  # Equivalent to len(my_list) - 2
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, 0)
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers([], 0)
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, 8)  # len(my_list) + 4
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, "H", 3, 4]
nb_print = safe_print_list_integers(my_list, 5)  # Equivalent to len(my_list)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "H", 4]
nb_print = safe_print_list_integers(my_list, 3)  # Equivalent to len(my_list) - 2
print("nb_print: {:d}".format(nb_print))

my_list = ["Holberton", 1, 2, "H", 3, 4, [1, 2, 3, 4]]
nb_print = safe_print_list_integers(my_list, 7)  # Equivalent to len(my_list)
print("nb_print: {:d}".format(nb_print))
