#!/usr/bin/python3
"""Module defining a Base class"""

import json


class Base:
    """Base class for managing ID"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list of dict): List of dictionaries to convert

        Returns:
            str: JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
