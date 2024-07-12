#!/usr/bin/python3
"""
This module defines the `inherits_from` function.
"""


def inherits_from(obj, a_class):
    """Checks if obj is an instance of a class that from a_class."""
    return issubclass(type(obj), a_class) and type(obj) != a_class
