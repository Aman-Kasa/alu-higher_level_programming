#!/usr/bin/python3
import json

"""
This module provides a base class for other classes in the project.

It includes functionality for managing object IDs and JSON serialization.
"""


class Base:
    """A base class for other classes in the project.

    This class manages the ID attribute and provides utility methods
    for JSON serialization.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): The ID to set for the instance. If None, a new ID
                      will be automatically assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list of dict): The list of dictionaries to
                                              serialize to JSON.

        Returns:
            str: The JSON string representation of the list of dictionaries.
                 If list_dictionaries is None or empty, returns "[]".
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
