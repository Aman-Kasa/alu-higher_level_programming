#!/usr/bin/python3
"""
This module defines the `MyList` class.
"""


class MyList(list):
    """A class that inherits from list anrder."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
