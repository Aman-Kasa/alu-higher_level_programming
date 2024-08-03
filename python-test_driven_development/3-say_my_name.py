#!/usr/bin/python3
"""
This module contains a function that prints a name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    Args:
        first_name (str): The first name.
        last_name (str): The last name (optional).

    Raises:
        TypeError: If either first_name or last_name is not a string.

    Examples:
    >>> say_my_name("John", "Smith")
    My name is John Smith
    >>> say_my_name("Walter", "White")
    My name is Walter White
    >>> say_my_name("Bob")
    My name is Bob
    >>> try:
    ...     say_my_name(12, "White")
    ... except Exception as e:
    ...     print(e)
    first_name must be a string
    >>> try:
    ...     say_my_name("John", 12)
    ... except Exception as e:
    ...     print(e)
    last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
