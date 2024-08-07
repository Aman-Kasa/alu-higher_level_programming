#!/usr/bin/python3
import json

"""
This module provides a base class for managing object IDs and JSON
serialization.

It includes:
- Base class for managing IDs.
- Static method for converting a list of dictionaries to a JSON string.
"""


class Base:
    """
    Base class for other classes in the project.

    Attributes:
        __nb_objects (int): The number of objects instantiated.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance.

        Args:
            id (int, optional): The ID to assign to the instance. If None,
                                a new ID will be automatically assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list of dict): The list of dictionaries to
                                              convert.

        Returns:
            str: The JSON string representation of the list of dictionaries.
                 Returns "[]" if list_dictionaries is None or empty.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
