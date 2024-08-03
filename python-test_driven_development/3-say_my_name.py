#!/usr/bin/python3
"""A function that prints the name of a user."""


def say_my_name(first_name, last_name=""):
    """
    Function to take in names and print the full name.
    Args:
        first_name (str): This is the first argument, and it must be a string.
        last_name (str): This is the second argument, default empty.
    Raises:
        TypeError: If either first_name or last_name is not a string.

    Returns:
        None
    Prints:
        My name is <first name> <last name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
