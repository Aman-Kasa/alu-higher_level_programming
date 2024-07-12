#!/usr/bin/python3
"""
This module defines the `is_same_class` function.
"""


def is_same_class(obj, a_class):
    """Checks if obj is exactly an instance of the specified class a_class."""
    return type(obj) == a_class
